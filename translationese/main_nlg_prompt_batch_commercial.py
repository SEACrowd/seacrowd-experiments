import os, sys
import csv
from os.path import exists

import pandas as pd
from tqdm import tqdm
from data_utils import load_instruction_tuning_datasets

import torch

from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, BloomTokenizerFast, set_seed
from nusacrowd.utils.constants import Tasks

from sacremoses import MosesTokenizer
import datasets, evaluate
from anyascii import anyascii
from retry import retry

import cohere

from dotenv import load_dotenv
import os
from openai import AzureOpenAI, BadRequestError, APIError

SEED=42
DEBUG=True

""" Generation metrics """
bleu = datasets.load_metric('bleu')
rouge = datasets.load_metric('rouge')
sacrebleu = datasets.load_metric('sacrebleu')
chrf = datasets.load_metric('chrf')
meteor = evaluate.load('meteor')
squad_v2_metric = datasets.load_metric('squad_v2')
mt = MosesTokenizer(lang='id')

def generation_metrics_fn(list_hyp, list_label):
    # hyp and label are both list of string
    # Check if the lists are empty
    if not list_hyp or not list_label or len(list_hyp) != len(list_label):
        raise ValueError("Input lists must be non-empty and of the same length")
    
    list_hyp = [hyp if hyp is not None else "" for hyp in list_hyp]
    list_label = [label if label is not None else "" for label in list_label]
    
    # Tokenize the hypotheses and labels for BLEU computation
    list_hyp_bleu = list(map(lambda x: mt.tokenize(x), list_hyp))
    list_label_bleu = list(map(lambda x: [mt.tokenize(x)], list_label))    
    list_label_sacrebleu = list(map(lambda x: [x], list_label))

    metrics = {}

    # Compute BLEU score
    try:
        metrics["BLEU"] = bleu._compute(list_hyp_bleu, list_label_bleu)['bleu'] * 100
    except ZeroDivisionError:
        metrics["BLEU"] = 0.0

    # Compute SacreBLEU score
    try:
        metrics["SacreBLEU"] = sacrebleu._compute(list_hyp, list_label_sacrebleu)['score']
    except ZeroDivisionError:
        metrics["SacreBLEU"] = 0.0

    # Compute chrF++ score
    try:
        metrics["chrF++"] = chrf._compute(list_hyp, list_label_sacrebleu)['score']
    except ZeroDivisionError:
        metrics["chrF++"] = 0.0

    # Compute METEOR score
    try:
        metrics["meteor"] = meteor.compute(predictions=list_hyp, references=list_label)['meteor'] * 100
    except ZeroDivisionError:
        metrics["meteor"] = 0.0

    # Compute ROUGE scores
    try:
        rouge_score = rouge._compute(list_hyp, list_label)
        metrics["ROUGE1"] = rouge_score['rouge1'].mid.fmeasure * 100
        metrics["ROUGE2"] = rouge_score['rouge2'].mid.fmeasure * 100
        metrics["ROUGEL"] = rouge_score['rougeL'].mid.fmeasure * 100
        metrics["ROUGELsum"] = rouge_score['rougeLsum'].mid.fmeasure * 100
    except ZeroDivisionError:
        metrics["ROUGE1"] = 0.0
        metrics["ROUGE2"] = 0.0
        metrics["ROUGEL"] = 0.0
        metrics["ROUGELsum"] = 0.0

    return metrics

def get_api_client(model):
    if "cohere" in model:
        client = cohere.Client(
            api_key=os.getenv("COHERE_PROD_API_KEY"),
        )
    elif "openai" in model:
        # Load secrets
        load_dotenv(dotenv_path=os.getenv("OPENAI_ENV_PATH"))
        client = AzureOpenAI(
            azure_endpoint = os.getenv("ENDPOINT"),
            api_key=os.getenv("API-KEY"),
            api_version="2024-02-01",
        )
    else:
        raise ValueError("Only support `cohere` and `openai` models.")  
    return client

# They sometimes timeout
@retry(Exception, tries=30, delay=10)
def get_response(
        client, model, prompt, temperature=0, max_output_tokens=200,
        system_message=""):
    if "cohere" in model:
        try:
            response = client.chat(
                model=model.split("/")[-1],
                message=prompt,
                preamble=system_message,
                temperature=temperature, # turn off randomness
                max_tokens=max_output_tokens, # keep it low because we only need the label choice for NLU
                seed=SEED,
            ).text
        except cohere.core.api_error.ApiError as e:
            response = "<BAD_REQUEST_ERROR>"
    elif "openai" in model:
        try:
            response = client.chat.completions.create(
                model=os.getenv("DEPLOYMENT-NAME"), # model = "deployment_name".
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_output_tokens,
                seed=SEED,
            )
            response = response.choices[0].message.content
        except BadRequestError as e:
            response = "<BAD_REQUEST_ERROR>"
        except APIError as e:
            response = "<BAD_REQUEST_ERROR>"
    else:
        raise ValueError("Only support `cohere` and `openai` models.")
    return response

def predict_generation(client, model, prompts):
    responses = []
    for prompt in prompts:
        response = get_response(client, model, prompt)
        if response is not None:
            responses.append(response.strip())
        else:
            responses.append("")
    return responses


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError('main_nlg_prompt.py <model_path_or_name> <n_batch>')

    # TODO: reduce hardcoded vars
    out_dir = './outputs_nlg'
    metric_dir = './metrics_nlg'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(metric_dir, exist_ok=True)

    MODEL = sys.argv[1]
    N_BATCH = int(sys.argv[2])
    SAVE_EVERY = 1

    # Load Dataset
    print('Load NLG Datasets...')
    nlg_datasets = load_instruction_tuning_datasets()

    print(f'Loaded {len(nlg_datasets)} NLG datasets')
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        print(f'{i} {dset_subset}')

    # Set seed
    set_seed(SEED)

    # Load Client
    client = get_api_client(MODEL)

    metrics = {'dataset': []}
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        nlg_dset, task_type = nlg_datasets[dset_subset]

        print(f"{i} {dset_subset} {task_type}")
        
        if nlg_dset is None:
            continue

        if 'test' in nlg_dset.keys():
            data = nlg_dset['test']
        elif 'devtest' in nlg_dset.keys():
            data = nlg_dset['devtest']
        elif 'validation' in nlg_dset.keys():
            data = nlg_dset['validation']
        else:
            data = nlg_dset['train']

        inputs = []
        preds = []
        preds_latin = []
        golds = []
        print(f"SAMPLE PROMPT: {data[0]['text_1']}")
        
        # Zero-shot inference
        if exists(f'{out_dir}/{dset_subset}_{MODEL.split("/")[-1]}.csv'):        
            print("Output exist, use existing log instead")
            with open(f'{out_dir}/{dset_subset}_{MODEL.split("/")[-1]}.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    inputs.append(row["Input"])
                    preds.append(row["Pred"])
                    preds_latin.append(row["Pred_Latin"])
                    golds.append(row["Gold"])
            print(f"Skipping until {len(preds)}")

        # If incomplete, continue
        if len(preds) < len(data):
            count = 0
            with torch.inference_mode():
                prompts, batch_golds = [], []
                for e, sample in enumerate(tqdm(data)):
                    if e < len(preds):
                        continue
                    
                    # Buffer
                    prompt_text = sample['text_1']
                    prompts.append(prompt_text)

                    batch_golds.append(sample['answer'][0] if 'answer' in sample else sample['text_2'])

                    # Batch inference
                    if len(prompts) == N_BATCH:
                        batch_preds = predict_generation(client, MODEL, prompts)
                        for (prompt_text, pred, gold) in zip(prompts, batch_preds, batch_golds):
                            inputs.append(prompt_text)
                            preds.append(pred if pred is not None else '')
                            preds_latin.append(anyascii(pred) if pred is not None else '')
                            golds.append(gold)
                        prompts, batch_golds = [], []
                        count += 1

                    if count == SAVE_EVERY:
                        # partial saving
                        inference_df = pd.DataFrame(list(zip(inputs, preds, preds_latin, golds)), columns=['Input', 'Pred', 'Pred_Latin', 'Gold'])
                        inference_df.to_csv(f'{out_dir}/{dset_subset}_{MODEL.split("/")[-1]}.csv', index=False)
                        count = 0

                # Predict the rest inputs
                if len(prompts) > 0:
                    batch_preds = predict_generation(client, MODEL, prompts)
                    for (prompt_text, pred, gold) in zip(prompts, batch_preds, batch_golds):
                        inputs.append(prompt_text)
                        preds.append(pred if pred is not None else '')
                        preds_latin.append(anyascii(pred) if pred is not None else '')
                        golds.append(gold)
                    prompts, batch_golds = [], []
            
            # Final save
            inference_df = pd.DataFrame(list(zip(inputs, preds, preds_latin, golds)), columns=['Input', 'Pred', 'Pred_Latin', 'Gold'])
            inference_df.to_csv(f'{out_dir}/{dset_subset}_{MODEL.split("/")[-1]}.csv', index=False)

            # To accomodate old bug where list are not properly re-initiated
            inputs = inputs[-len(data):]
            preds = preds[-len(data):]
            preds_latin = preds_latin[-len(data):]
            golds = golds[-len(data):]

            eval_metric = generation_metrics_fn(preds, golds)
            eval_metric_latin = generation_metrics_fn(preds_latin, golds)
            for key, value in eval_metric_latin.items():
                eval_metric[f'{key}_latin'] = value

            print(f'== {dset_subset} == ')
            for k, v in eval_metric.items():
                print(k, v)            
            print("===\n\n")
            eval_metric['prompt_id'] = 0

            metrics['dataset'].append(dset_subset)
            for k in eval_metric:
                if k not in metrics:
                    metrics[k] = []
                metrics[k].append(eval_metric[k])


    pd.DataFrame.from_dict(metrics).reset_index().to_csv(f'{metric_dir}/nlg_results_{MODEL.split("/")[-1]}.csv', index=False)

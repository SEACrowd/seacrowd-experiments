import os, sys
import csv
from os.path import exists

import pandas as pd
from tqdm import tqdm
from prompt_utils import get_prompt, get_lang_name
from data_utils import load_nlg_datasets

import json
import torch
from openai import OpenAI

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
    if "openai" in model:
        client = OpenAI(api_key=os.getenv("OPENAI_BATCH_API_KEY"))
    else:
        raise ValueError("Only support `openai` models.")  
    return client

# They sometimes timeout
@retry(Exception, tries=30, delay=10)
def get_response(
        client, model, prompt, temperature=0, max_output_tokens=200,
        system_message="Only respond with the answer."):
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
                model=model, # model = "deployment_name".
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

def convert_prompts_to_batch_file(
    prompts, dset_subset, prompt_lang, prompt_id,
    temperature=0, max_output_tokens=200, system_message="Only respond with the answer."):

    file_path = f'./batch_files_nlg/{dset_subset}_{prompt_lang}_{prompt_id}.jsonl'

    with open(file_path, 'w') as f:
        for i, prompt in enumerate(prompts):
            line = {
                "custom_id": f"{dset_subset}_{prompt_lang}_{prompt_id}_{i}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "gpt-4o",
                    "messages": [
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompts[i]}
                    ],
                    "max_tokens": max_output_tokens,
                    "temperature": temperature,
                    "seed": SEED
                }
            }
            print(json.dumps(line), file=f)
    return file_path

def to_prompt(input, prompt, prompt_lang, task_name, task_type, with_label=False, use_template=False):
    if '[INPUT]' in prompt:
        prompt = prompt.replace('[INPUT]', input['text_1'])

    if task_type == Tasks.MACHINE_TRANSLATION.value:

        # Extract src and tgt based on nusantara config name
        task_names = task_name.split('_')

        if "flores200" in task_name:
            src_lang = task_names[-6]
            tgt_lang = task_names[-4]

        else:
            src_lang = task_names[-4]
            tgt_lang = task_names[-3]

        # Replace src and tgt lang name
        prompt = prompt.replace('[SOURCE]', get_lang_name(prompt_lang, src_lang))
        prompt = prompt.replace('[TARGET]', get_lang_name(prompt_lang, tgt_lang))
    
    if task_type == Tasks.QUESTION_ANSWERING.value:
        prompt = prompt.replace('[CONTEXT]', input['context'])
        prompt = prompt.replace('[QUESTION]', input['question'])
    
    if with_label:
        if task_type == Tasks.QUESTION_ANSWERING.value:
            prompt += " " + input['answer'][0]
        else:
            prompt += " " + input['text_2']

    if use_template:
        prompt_template = "### USER:\n{human_prompt}\n\n### RESPONSE:\n"
        prompt = prompt_template.format(human_prompt=prompt)
    
    return prompt

def predict_generation(client, model, prompts):
    responses = []
    for prompt in prompts:
        response = get_response(client, model, prompt)
        if response is not None:
            responses.append(response.strip())
        else:
            responses.append("")
    return responses


def send_batch(prompt_lang, MODEL, batch_file_dir='./batch_files_nlg'):
    
    os.makedirs(batch_file_dir, exist_ok=True)

    # Load prompt
    prompt_templates = get_prompt(prompt_lang, return_only_one=True) # Commercial only needs ONE prompt per task

    # Load Dataset
    print('Load NLG Datasets...')
    nlg_datasets = load_nlg_datasets()

    print(f'Loaded {len(nlg_datasets)} NLG datasets')
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        print(f'{i} {dset_subset}')

    # Set seed
    set_seed(SEED)

    # Load Client
    client = get_api_client(MODEL)

    for i, dset_subset in enumerate(nlg_datasets.keys()):
        nlg_dset, task_type = nlg_datasets[dset_subset]

        print(f"{i} {dset_subset} {task_type}")
        
        if task_type.value not in prompt_templates or nlg_dset is None:
            continue

        if 'test' in nlg_dset.keys():
            data = nlg_dset['test']
        elif 'devtest' in nlg_dset.keys():
            data = nlg_dset['devtest']
        elif 'validation' in nlg_dset.keys():
            data = nlg_dset['validation']
        else:
            data = nlg_dset['train']

        # data = data.shard(100, 0) # get shard the size of the dataset for efficiency

        for prompt_id, prompt_template in enumerate(prompt_templates[task_type.value]):
            prompts = []
            golds = []  
            print(f"PROMPT ID: {prompt_id}")
            print(f"SAMPLE PROMPT: {to_prompt(data[0], prompt_template, prompt_lang, dset_subset, task_type.value)}")

            # CANNOT CONTINUE FROM WHERE IT LEFT OFF
            for e, sample in enumerate(tqdm(data)):
                # Buffer
                prompt_text = to_prompt(sample, prompt_template, prompt_lang, dset_subset, task_type.value)
                # prompt_text = '\n\n'.join(few_shot_text_list + [prompt_text])
                prompts.append(prompt_text)

                golds.append(sample['answer'][0] if 'answer' in sample else sample['text_2'])

            # Convert prompts to batch file
            print("CONVERT PROMPTS TO BATCH FILE")
            batch_file_path = convert_prompts_to_batch_file(prompts, dset_subset, prompt_lang, prompt_id)

            # Upload batch file
            batch_input_file = client.files.create(
                file=open(batch_file_path, "rb"),
                purpose="batch",
            )

            # Create batch
            batch = client.batches.create(
                input_file_id=batch_input_file.id,
                endpoint="/v1/chat/completions",
                completion_window="24h",
                metadata={"description": f"{dset_subset}_{prompt_lang}_{prompt_id}"}
            )

            print("=== BATCH ID:", batch.id, "===")

            with open(f'{batch_file_dir}/batch_{dset_subset}_{prompt_lang}_{prompt_id}_{MODEL.split("/")[-1]}.json', 'w') as f:
                batch_metadata = {
                    "id": batch.id,
                    "completion_window": batch.completion_window,
                    "created_at": batch.created_at,
                    "endpoint": batch.endpoint,
                    "input_file_id": batch.input_file_id,
                    "metadata": batch.metadata,

                }
                print(json.dumps(batch_metadata), file=f)
    return 0


def parse_output(prompt_lang, MODEL, out_dir='./outputs_nlg', metric_dir='./metrics_nlg', batch_file_dir='./batch_files_nlg'):

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(metric_dir, exist_ok=True)
    os.makedirs(batch_file_dir, exist_ok=True)

    # Load prompt
    prompt_templates = get_prompt(prompt_lang, return_only_one=True) # Commercial only needs ONE prompt per task
    
    # Load Dataset
    print('Load NLG Datasets...')
    nlg_datasets = load_nlg_datasets()

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

        print()
        print("==============================")
        print(f"{i} {dset_subset} {task_type}")
        
        if task_type.value not in prompt_templates or nlg_dset is None:
            continue

        if 'test' in nlg_dset.keys():
            data = nlg_dset['test']
        elif 'devtest' in nlg_dset.keys():
            data = nlg_dset['devtest']
        elif 'validation' in nlg_dset.keys():
            data = nlg_dset['validation']
        else:
            data = nlg_dset['train']

        for prompt_id, prompt_template in enumerate(prompt_templates[task_type.value]):
            batch_file_name = f'{dset_subset}_{prompt_lang}_{prompt_id}'
            batch_meta_file_path = f'{batch_file_dir}/batch_{batch_file_name}_{MODEL.split("/")[-1]}.json'
            
            inputs, preds, preds_latin, golds = [], [], [], []

            inference_csv_path = f'{out_dir}/{batch_file_name}_0_{MODEL.split("/")[-1]}.csv'
            output_file_path = f'{batch_file_dir}/output_file_{batch_file_name}_{MODEL.split("/")[-1]}.jsonl'

            if not os.path.isfile(inference_csv_path):
            # if True:
                if not os.path.isfile(output_file_path):
                    if not os.path.isfile(batch_meta_file_path):
                        raise ValueError("Batch meta file not found:", batch_meta_file_path)

                    with open(batch_meta_file_path, 'r') as f:
                        batch_metadata = json.load(f)
                        batch_id = batch_metadata['id']

                    print(f"=== {batch_file_name} | BATCH ID: {batch_id} ===")

                    found = False
                    for batch in client.batches.list(limit=100).data:
                        if not found and batch.id == batch_id:
                            found = True
                            if batch.status != "completed":
                                print("Status:", batch.status)
                                return
                            
                            print("HELLOLOOOLOLOLOL")
                            content = client.files.content(batch.output_file_id)
                            with open(output_file_path, 'w+') as f:
                                f.write(content.content.decode('utf-8').strip())
                    if not found:
                        # raise ValueError("Batch not found:", batch_id)
                        print("Batch not found:", batch_id)
                        continue

            if os.path.isfile(output_file_path):
                output_dict = {}
                with open(output_file_path, 'r+') as output_file:
                    for line in output_file:
                        line_dict = json.loads(line)
                        output_dict[line_dict["custom_id"]] = line_dict["response"]["body"]["choices"][0]["message"]["content"]

                with open(f'{batch_file_dir}/{batch_file_name}.jsonl', 'r+') as input_file:
                    for i, line in enumerate(input_file):
                        line_dict = json.loads(line)
                        custom_id = line_dict["custom_id"]
                        inputs.append(line_dict["body"]["messages"][1]["content"])

                        if custom_id not in output_dict:
                            response = get_response(
                                client, MODEL.split("/"), line_dict["body"]["messages"][1]["content"])
                            with open(output_file_path, 'a') as output_file:
                                output_file.write("\n" +
                                    json.dumps(
                                        {
                                            "custom_id": custom_id,
                                            "response": {
                                                "body": {
                                                    "choices": [
                                                        {"message": {"content": response}}
                                                    ]
                                                }
                                            }
                                        }
                                    )
                                )
                            output_dict[custom_id] = response

                        preds.append(output_dict[custom_id])
                        preds_latin.append(anyascii(output_dict[custom_id]))
                        golds.append(data[i]['answer'][0] if 'answer' in data[i] else data[i]['text_2'])

                if len(inputs) == len(data):
                    # Final save
                    inference_df = pd.DataFrame(
                        list(zip(inputs, preds, preds_latin, golds)),
                        columns=['Input', 'Pred', 'Pred_Latin', 'Gold'])
                    inference_df.to_csv(inference_csv_path, index=False)
                else:
                    print(dset_subset, len(inputs), len(data))
                
            inference_df = pd.read_csv(inference_csv_path)

            inputs = inference_df['Input'].tolist()
            preds = inference_df['Pred'].fillna("").tolist()
            preds_latin = inference_df['Pred_Latin'].fillna("").tolist()
            golds = inference_df['Gold'].fillna("").tolist()

            if len(preds) > 0:
                eval_metric = generation_metrics_fn(preds, golds)
                eval_metric_latin = generation_metrics_fn(preds_latin, golds)
                for key, value in eval_metric_latin.items():
                    eval_metric[f'{key}_latin'] = value

                print(f'== {dset_subset} == ')
                for k, v in eval_metric.items():
                    print(k, v)            
                print("===\n\n")
                eval_metric['prompt_id'] = prompt_id

                metrics['dataset'].append(dset_subset)
                for k in eval_metric:
                    if k not in metrics:
                        metrics[k] = []
                    metrics[k].append(eval_metric[k])

    pd.DataFrame.from_dict(metrics).reset_index().to_csv(f'{metric_dir}/nlg_results_{prompt_lang}_0_{MODEL.split("/")[-1]}.csv', index=False)

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError('main_nlg_prompt.py <mode> <prompt_lang> <model_path_or_name>')

    mode = sys.argv[1]
    prompt_lang = sys.argv[2]
    MODEL = sys.argv[3]

    if mode == "send_batch":
        send_batch(prompt_lang, MODEL)
    elif mode == "parse_output":
        parse_output(prompt_lang, MODEL)
    else:
        raise ValueError("Only handles `send_batch` and `parse_output` modes.")
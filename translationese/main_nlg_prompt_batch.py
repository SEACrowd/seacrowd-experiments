import os, sys
import csv
from os.path import exists

import pandas as pd
from tqdm import tqdm
from data_utils import load_instruction_tuning_datasets

import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, BloomTokenizerFast, set_seed
from nusacrowd.utils.constants import Tasks

from sacremoses import MosesTokenizer
import datasets, evaluate
from anyascii import anyascii
from retry import retry


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


def predict_generation(prompts, model_name, tokenizer, model):
    #model = model.to('cuda')

    if "Qwen" in model_name:
        preds = []
        for prompt in prompts:
            pred, _ = model.chat(tokenizer, prompt, history=None)
            preds.append(pred)
        return preds
    else:
        inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=1024).to('cuda')
        input_size = inputs["input_ids"].shape[1]

        if "sea-lion" in model_name:
            inputs.pop("token_type_ids", None)
        
        if model.config.is_encoder_decoder:
            outputs = model.generate(**inputs, do_sample=True, min_length=1, max_length=100)
            preds = tokenizer.batch_decode(outputs, skip_special_tokens=True) 
            return preds
        else:
            outputs = model.generate(**inputs, do_sample=True, min_length=input_size+1, max_length=input_size+100)
            if "llama" in model_name:
                preds = [p.strip() for p in tokenizer.batch_decode(outputs[:,inputs["input_ids"].shape[1]:], skip_special_tokens=True)]
            else:
                preds = tokenizer.batch_decode(outputs[:,inputs["input_ids"].shape[1]:], skip_special_tokens=True)
            return preds


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
    SAVE_EVERY = 10

    # Load Dataset
    print('Load NLG Datasets...')
    nlg_datasets = load_instruction_tuning_datasets()

    print(f'Loaded {len(nlg_datasets)} NLG datasets')
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        print(f'{i} {dset_subset}')

    # Set seed
    set_seed(42)

    # Load Model & Tokenizer
    # Tokenizer initialization
    use_prompt_template = "sea-lion" in MODEL and "instruct" in MODEL
    tokenizer = AutoTokenizer.from_pretrained(MODEL, truncation_side='left', trust_remote_code=True)
    tokenizer.padding_side = "left"

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.bos_token if tokenizer.bos_token is not None else tokenizer.eos_token
    
    if "Qwen" in MODEL:
        tokenizer.add_special_tokens({'pad_token': '<|endoftext|>'})

    # Model initialization
    fp16_args = {'device_map': "auto", 'torch_dtype': torch.float16, 'load_in_8bit': True}  # needed for larger model
    if "aya-101" in MODEL:
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL, device_map="auto", load_in_8bit=True, trust_remote_code=True, resume_download=True)
    elif "mt0" in MODEL or "mt5" in MODEL:
        extra_args = fp16_args if "xxl" in MODEL else {}
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL, resume_download=True, trust_remote_code=True, **extra_args)
        if "xxl" not in MODEL:
            model = model.to('cuda')
    else:
        extra_args = fp16_args if "7b" in MODEL.lower() or "13b" in MODEL.lower() or "8b" in MODEL.lower() else {}
        model = AutoModelForCausalLM.from_pretrained(MODEL, resume_download=True, trust_remote_code=True, **extra_args)
        if "SeaLLM" in MODEL or "Qwen" in MODEL or 'falcon' in MODEL:
            #if "SeaLLM" in MODEL or "llama" in MODEL:
            # quick fix for tensor error
            # https://github.com/facebookresearch/llama/issues/380
            model = model.bfloat16()
    
    if model is not None:
        #model.cuda()
        model.eval()

    metrics = {'dataset': []}
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        nlg_dset, task_type = nlg_datasets[dset_subset]

        print(f"{i} {dset_subset} {task_type}")
        
        if nlg_dset is None:
            continue

        if 'test' in nlg_dset.keys():
            data = nlg_dset['test']
        elif 'validation' in nlg_dset.keys():
            data = nlg_dset['validation']
        elif 'devtest' in nlg_dset.keys():
            data = nlg_dset['devtest']
        else:
            data = nlg_dset['train']

        #data = data.shard(10000, 0) # get shard the size of the dataset for efficiency

        if 'train' in nlg_dset.keys():
            few_shot_data = nlg_dset['train']
        elif 'devtest' in nlg_dset.keys():
            few_shot_data = nlg_dset['devtest']
        elif 'test' in nlg_dset.keys():
            few_shot_data = nlg_dset['test']

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
                        batch_preds = predict_generation(prompts, MODEL, tokenizer, model)
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
                    batch_preds = predict_generation(prompts, MODEL, tokenizer, model)
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

"""nusacrowd zero-shot prompt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ru8DyS2ALWfRdkjOPHj-KNjw6Pfa44Nd
"""
import csv
import jiwer
import json
import os
import pandas as pd
import re
import string
import sys
import torch
import torch.nn.functional as F
import torchaudio
from dataclasses import dataclass, field
from numpy import argmax, stack
from os.path import exists
from peft import PeftModel
from sklearn.metrics import classification_report, precision_recall_fscore_support
from tqdm import tqdm
from transformers import (
    set_seed,
    Wav2Vec2Processor,
    Wav2Vec2CTCTokenizer,
    Wav2Vec2FeatureExtractor,
    Wav2Vec2ForCTC,
    Wav2Vec2Config,
    Trainer,
    TrainingArguments,
    HfArgumentParser,
    EarlyStoppingCallback
)
from typing import Any, Dict, List, Optional, Union

from data_utils import load_speech_datasets
from prompt_utils import get_prompt, get_label_mapping

# !pip install git+https://github.com/IndoNLP/nusa-crowd.git@release_exp
# !pip install transformers
# !pip install sentencepiece

DEBUG = False

csv.field_size_limit(sys.maxsize)

#####
# Common Functions
#####
CHARS_TO_IGNORE = [",", "?", "¿", ".", "!", "¡", ";", "；", ":", '""', "%", '"', "�", "ʿ", "·", "჻", "~", "՞",
                   "؟", "،", "।", "॥", "«", "»", "„", "“", "”", "「", "」", "‘", "’", "《", "》", "(", ")",
                   "{", "}", "=", "`", "_", "+", "<", ">", "…", "–", "°", "´", "ʾ", "‹", "›", "©", "®", "—", "→", "。",
                   "、", "﹂", "﹁", "‧", "～", "﹏", "，", "｛", "｝", "（", "）", "［", "］", "【", "】", "‥", "〽",
                   "『", "』", "〝", "〟", "⟨", "⟩", "〜", "：", "！", "？", "♪", "؛", "/", "\\", "º", "−", "^", "ʻ", "ˆ"]

chars_to_ignore_re = f"[{re.escape(''.join(CHARS_TO_IGNORE))}]"

DEFAULT_SAMPLING_RATE = 16000

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError('main_speech_no_prompt_batch.py <model_path_or_name> <batch_size> <save_every (OPTIONAL)>')

    MODEL = sys.argv[1]
    BATCH_SIZE = int(sys.argv[2])
    ADAPTER = ''

    SAVE_EVERY = 10
    if len(sys.argv) == 4:
        SAVE_EVERY = int(sys.argv[3])

    out_dir = './outputs_speech'
    metric_dir = './metrics_speech'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(metric_dir, exist_ok=True)
    gpu = 0
    device = torch.device(f"cuda:{gpu}" if torch.cuda.is_available() else "cpu")


    def remove_special_characters(batch):
        batch["text"] = re.sub(chars_to_ignore_re, '', batch["text"]).lower().replace("’", "'")
        return batch


    def extract_all_chars(batch):
        all_text = " ".join([text.lower() for text in batch["text"]])
        vocab = list(set(all_text))
        return {"vocab": [vocab], "all_text": [all_text]}

    # Define compute metric function
    def compute_metrics(pred):
        pred_strs = pred["predicted"]
        label_strs = pred["target"]
        if len(label_strs) == 0:
            return 0, 0
        else:
            wer = jiwer.wer(pred_strs, label_strs)
            mer = jiwer.mer(pred_strs, label_strs)
            cer = jiwer.cer(pred_strs, label_strs)

        metrics = {
            "wer": wer, "mer": mer, "cer": cer
        }

        return metrics


    # MAIN FLOW STARTS HERE
    # Set seed before initializing model.
    set_seed(42)

    # Load Dataset
    print('Load Speech Datasets...')
    speech_datasets = load_speech_datasets()

    print(f'Loaded {len(speech_datasets)} Speech datasets')

    # Load Model
    print('Load Wav2Vec2 model and processor...')

    processor = Wav2Vec2Processor.from_pretrained(MODEL)
    model = Wav2Vec2ForCTC.from_pretrained(MODEL).cuda()


    def map_to_array(batch):
        speech, sr = torchaudio.load(batch["path"])
        if sr != DEFAULT_SAMPLING_RATE:
            resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=DEFAULT_SAMPLING_RATE)
            batch["speech"] = resampler.forward(speech.squeeze(0)).numpy()
            batch["sampling_rate"] = DEFAULT_SAMPLING_RATE
        else:
            batch["speech"] = speech.squeeze(0)
        batch["sentence"] = batch["text"]
        return batch


    def map_to_pred(batch):
        features = processor(batch["speech"], sampling_rate=DEFAULT_SAMPLING_RATE, padding=True, return_tensors="pt")
        with torch.no_grad():    
            input_values = features.input_values
            attention_mask = features.attention_mask
            logits = model(input_values.to("cuda"), attention_mask.to("cuda")).logits
        pred_ids = torch.argmax(logits, dim=-1)
        batch["predicted"] = processor.batch_decode(pred_ids)
        batch["target"] = batch["sentence"]
        return batch


    metrics_all = []
    for i, dset_subset in enumerate(speech_datasets.keys()):
        speech_dataset, task = speech_datasets[dset_subset]
        print(f"=== ({i}/{len(speech_datasets.keys())}) {dset_subset} ===")
        # Evaluation Phase (Test)
        if "test" in speech_dataset.keys():
            print("*** Test Phase ***")
            ds = speech_dataset["test"].map(map_to_array)
            result = ds.map(map_to_pred, batched=True, batch_size=BATCH_SIZE, remove_columns=list(ds.features.keys()))
            metrics = compute_metrics(result)
            metrics_all.append({
                'dataset': dset_subset,
                'fold': 'test',
                'wer': metrics["wer"],
                'mer': metrics["mer"],
                'cer': metrics["cer"]
            })

    pd.DataFrame(metrics_all).reset_index().to_csv(
        f'{metric_dir}/speech_results_{MODEL.split("/")[-1]}.csv',
        index=False
    )

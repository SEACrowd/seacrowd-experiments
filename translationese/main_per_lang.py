import os

import glob
import numpy as np
import pandas as pd
from tqdm import tqdm

import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader

import datasets
from transformers import AutoTokenizer, AutoModelForSequenceClassification, EarlyStoppingCallback
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding
import evaluate

from sklearn.model_selection import train_test_split
import argparse

# Evaluation Metric
metric_acc = evaluate.load("accuracy")
metric_prec = evaluate.load("precision")
metric_rec = evaluate.load("recall")
metric_f1 = evaluate.load("f1")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = metric_acc.compute(predictions=preds, references=labels)['accuracy']
    prec = metric_prec.compute(predictions=preds, references=labels, average='weighted')['precision']
    rec = metric_rec.compute(predictions=preds, references=labels, average='weighted')['recall']
    f1 = metric_f1.compute(predictions=preds, references=labels, average='weighted')['f1']
    return {'acc': acc, 'prec': prec, 'rec': rec, 'f1': f1}

if __name__ == '__main__':
    # Parse Argument
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('--model_path', type=str, default='FacebookAI/xlm-roberta-base', help='Model path')
    parser.add_argument('--ouput_dir', type=str, default='./runs', help='Output directory')
    parser.add_argument('--logging_dir', type=str, default='./logs', help='Output directory')
    parser.add_argument('--batch_size', type=int, default=512, help='Batch size')
    parser.add_argument('--n_epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--lr', type=float, default=5e-5, help='Learning rate')
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1, help='Gradient accumulation steps')
    args = parser.parse_args()

    model_path = args.model_path
    out_dir = args.ouput_dir
    log_dir = args.logging_dir
    bs = args.batch_size
    n_epochs = args.n_epochs
    lr = args.lr
    grad_accum = args.gradient_accumulation_steps

    os.makedirs('./results', exist_ok=True)
    os.makedirs('./cached_data_per_lang', exist_ok=True)
    
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Load Dataset
    def tokenize(example):
        inputs = tokenizer(str(example['text']), padding='longest', max_length=512, truncation=True)
        inputs['labels'] = example['label']
        return inputs

    if os.path.exists(f'./cached_data_per_lang/{model_path.split("/")[-1]}'):
        dset = datasets.load_from_disk(f'./cached_data_per_lang/{model_path.split("/")[-1]}')
    else:
        dset = datasets.load_dataset('SEACrowd/sea_translationese_resampling')        
        dset = dset.class_encode_column("label")
        dset = dset.map(tokenize, batched=False, remove_columns=['label', 'text'])
        dset.save_to_disk(f'./cached_data_per_lang/{model_path.split("/")[-1]}')

    train_valid_dset, test_dset = dset['train'], dset['test']
    train_valid_dset = train_valid_dset.train_test_split(test_size=1000, seed=14045)
    train_dset, valid_dset = train_valid_dset['train'], train_valid_dset['test']

    dset_dict = {}
    train_df, valid_df, test_df = train_dset.to_pandas(), valid_dset.to_pandas(), test_dset.to_pandas()
    langs = train_df['lang'].unique().tolist()
    for lang in langs:
        if os.path.exists(f'./results/eval_results_{lang}.pt'):
            print(f'Skipping {lang}...')
            valid_results, eval_results = torch.load(f'./results/eval_results_{lang}.pt')
        else:
            train_dset = datasets.Dataset.from_pandas(train_df.loc[train_df['lang'] == lang,:])
            valid_dset = datasets.Dataset.from_pandas(valid_df.loc[valid_df['lang'] == lang,:])
            test_dset = datasets.Dataset.from_pandas(test_df.loc[test_df['lang'] == lang,:])
        
            # Load Model
            model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=len(set(test_dset['labels'])))
        
            # Define the data collator
            data_collator = DataCollatorWithPadding(tokenizer)
        
            # Define the training arguments
            training_args = TrainingArguments(
                output_dir=out_dir,                   # Output directory
                logging_dir=log_dir,                  # Logging directory
                num_train_epochs=n_epochs,            # Number of training epochs
                per_device_train_batch_size=bs,       # Batch size for training
                per_device_eval_batch_size=bs,        # Batch size for evaluation
                gradient_accumulation_steps=grad_accum,  # Gradient accumulation steps
                learning_rate=lr,                     # Learning rate
                warmup_steps=20,                      # Number of warmup steps
                weight_decay=0.01,                    # Weight decay
                logging_steps=10,                     # Log every X steps
                evaluation_strategy='epoch',          # Evaluation strategy
                save_strategy='epoch',                # Save strategy
                save_total_limit=3,                   # Limit the total number of checkpoints
                load_best_model_at_end=True,          # Load the best model at the end of training
                metric_for_best_model='valid_loss',   # Metric to use to select the best model
                greater_is_better=False,              # Whether the higher value of the metric is better
                gradient_checkpointing=True,          # Gradient checkpointing
                bf16=True,                            # FP16
                save_steps=1,                         # Save model every epoch
                report_to='tensorboard'               # Report to
            )
        
            # Define the trainer
            trainer = Trainer(
                model=model,                                            # The model to train
                args=training_args,                                     # Training arguments
                train_dataset=train_dset,                               # Training dataset
                eval_dataset={'valid': valid_dset, 'test': test_dset},  # Evaluation dataset
                data_collator=data_collator,                            # Data collator
                compute_metrics=compute_metrics,                        # Metrics to compute
                callbacks=[EarlyStoppingCallback(early_stopping_patience=3)] # Early stopping patience
            )
        
            # Train the model
            trainer.train()
        
            # Evaluate the model on the test dataset
            valid_results = trainer.predict(valid_dset)
            eval_results = trainer.predict(test_dset)
        torch.save((valid_results, eval_results), f'./results/eval_results_{lang}.pt')
    
        # Print the evaluation results
        print(f'=== {lang} ===')
        print('== Validation ==')
        print(valid_results.metrics)
        print('== Evaluation ==')
        print(eval_results.metrics)
        print('=============')
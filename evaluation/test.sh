CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng bigscience/mt0-xl 0 4
CUDA_VISIBLE_DEVICES=6 python main_nlg_prompt_batch.py eng indonlp/cendol-mt5-xl 0 4
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng bigscience/bloomz-7b1 0 4
CUDA_VISIBLE_DEVICES=7 python main_nlg_prompt_batch.py eng MBZUAI/bactrian-x-llama-7b-merged 0 4
CUDA_VISIBLE_DEVICES=5 python main_nlg_prompt_batch.py eng mistralai/Mistral-7B-Instruct-v0.2 0 4
#CUDA_VISIBLE_DEVICES=5 python main_nlg_prompt_batch.py eng meta-llama/Meta-Llama-3-8B-Instruct 0 4
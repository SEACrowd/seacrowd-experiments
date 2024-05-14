#huggingface-cli login --token $HF_TOKEN

####
# Zero-Shot 3B Eng
####

# mT0
CUDA_VISIBLE_DEVICES=7 python main_nlg_prompt_batch.py eng bigscience/mt0-xl 0 4 &

# Cendol-Instruct mT5
CUDA_VISIBLE_DEVICES=7 python main_nlg_prompt_batch.py eng indonlp/cendol-mt5-xl 0 4 &

# # ####
# # # Zero-Shot 7B Eng
# # ####

# Multilingual - BLOOMZ
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng bigscience/bloomz-7b1 0 4 &

# Multilingual - Bactrian-X
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng MBZUAI/bactrian-x-llama-7b-merged 0 4 &

# Multilingual - Mistral
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng mistralai/Mistral-7B-Instruct-v0.2 0 4 &

# Llama 3
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng meta-llama/Meta-Llama-3-8B-Instruct 0 4 &

# # English - Falcon
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng tiiuae/falcon-7b-instruct 4 &

# # Bilingual Eng/Chinese - Qwen
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng Qwen/Qwen-7B-Chat 4 &

# # SEA - SEA-LION -- weird error: TypeError: MPTForCausalLM.forward() got an unexpected keyword argument |'token_type_ids' | will check later
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng aisingapore/sea-lion-7b-instruct-research 4 &

# # SEA - SeaLLMs 2.5
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng SeaLLMs/SeaLLM-7B-v2.5 4 &

# # SEA - SAILOR
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng sail/Sailor-7B-Chat 4 &

# # Indo - Cendol-Instruct LLaMA2
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng indonlp/cendol-llama2-7b 4 &

# # Indo - Merak-7B-v4
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng Ichsan2895/Merak-7B-v4 4 &

# # Vietnamese - PhoGPT
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng vinai/PhoGPT-7B5-Instruct 4 &

# ####
# # Zero-Shot 13B Eng
# ####

# # AYA
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng CohereForAI/aya-101 4 &
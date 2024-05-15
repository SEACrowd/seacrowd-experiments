#huggingface-cli login --token $HF_TOKEN

####
# Zero-Shot 3B Eng
####

# mT0 --> Holy
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng bigscience/mt0-xl 0 4 &

# Cendol-Instruct mT5 --> Holy
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng indonlp/cendol-mt5-xl 0 4 &

# # ####
# # # Zero-Shot 7B Eng
# # ####

# # Multilingual - BLOOMZ --> Ruochen
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng bigscience/bloomz-7b1 0 4 &

# # Multilingual - Bactrian-X --> Ruochen
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng MBZUAI/bactrian-x-llama-7b-merged 0 4 &

# # Multilingual - Mistral --> Joseph
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng mistralai/Mistral-7B-Instruct-v0.2 0 4 &

# # Llama 3 --> Joseph
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng meta-llama/Meta-Llama-3-8B-Instruct 0 4 &

# # English - Falcon --> Ruochen
# CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py eng tiiuae/falcon-7b-instruct 0 4 &

# # Bilingual Eng/Chinese - Qwen
# CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng Qwen/Qwen-7B-Chat 0 4 &

# # SEA - SEA-LION --> Holy
# CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng aisingapore/sea-lion-7b-instruct-research 0 4 &

# # SEA - SeaLLMs 2.5 --> Fajri
# CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng SeaLLMs/SeaLLM-7B-v2.5 0 4 &

# # SEA - SAILOR
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng sail/Sailor-7B-Chat 0 4 &

# # Indo - Cendol-Instruct LLaMA2 --> Fajri
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng indonlp/cendol-llama2-7b 0 4 &

# # Indo - Merak-7B-v4 --> Fajri
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng Ichsan2895/Merak-7B-v4 0 4 &

# # Vietnamese - PhoGPT
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng vinai/PhoGPT-7B5-Instruct 0 4 &

# ####
# # Zero-Shot 13B Eng
# ####

# # AYA --> Holy
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng CohereForAI/aya-101 0 2 &
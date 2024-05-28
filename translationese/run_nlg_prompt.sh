#huggingface-cli login --token $HF_TOKEN

####
# Zero-Shot 3B Eng
####

# mT0 --> Holy
CUDA_VISIBLE_DEVICES=7 python main_nlg_prompt_batch.py bigscience/mt0-xl 4 &

# Cendol-Instruct mT5 --> Holy
CUDA_VISIBLE_DEVICES=7 python main_nlg_prompt_batch.py indonlp/cendol-mt5-xl 4 &

# # ####
# # # Zero-Shot 7B Eng
# # ####

# # AYA-23 --> Holy
# CUDA_VISIBLE_DEVICES=5 python main_nlg_prompt_batch.py CohereForAI/aya-23-8B 4 &

# # Multilingual - BLOOMZ --> Ruochen
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py bigscience/bloomz-7b1 4 &

# # Multilingual - Bactrian-X --> Ruochen
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py MBZUAI/bactrian-x-llama-7b-merged 4 &

# # Multilingual - Mistral --> Joseph
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py mistralai/Mistral-7B-Instruct-v0.2 4 &

# # Llama 3 --> Joseph
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py meta-llama/Meta-Llama-3-8B-Instruct 4 &

# # English - Falcon --> Ruochen
# CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py tiiuae/falcon-7b-instruct 4 &

# # Bilingual Eng/Chinese - Qwen --> Holy
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py Qwen/Qwen-7B-Chat 2 &

# # SEA - SEA-LION --> Holy
# CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py aisingapore/sea-lion-7b-instruct-research 32 &

# # SEA - SeaLLMs 2.5 --> Holy/Fajri
# CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py SeaLLMs/SeaLLM-7B-v2.5 4 &

# # SEA - SAILOR --> Holy
# CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py sail/Sailor-7B-Chat 16 &

# # Indo - Cendol-Instruct LLaMA2 --> Holy/Fajri
# CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py indonlp/cendol-llama2-7b 8 &

# # Indo - Merak-7B-v4 --> Holy/Fajri
# CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py Ichsan2895/Merak-7B-v4 16 &

# # Vietnamese - PhoGPT --> Gated model, never got the approval
# CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py vinai/PhoGPT-7B5-Instruct 4 &

# # Thai - WangchanX LLaMa3 --> Peerat
# CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py airesearch/LLaMa3-8b-WangchanX-sft-Demo 4 &

# # Malay - Malaysian Llama3 --> Peerat
# CUDA_VISIBLE_DEVICES=5 python main_nlg_prompt_batch.py mesolitica/malaysian-llama-3-8b-instruct-16k 4 &

# ####
# # Zero-Shot 13B Eng
# ####

# AYA --> Holy
CUDA_VISIBLE_DEVICES=6 python main_nlg_prompt_batch.py CohereForAI/aya-101 2 &
huggingface-cli login --token $HF_TOKEN

####
# Zero-Shot 3B Eng
####

# # mT0
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng bigscience/mt0-xl 4 &

# # Cendol-Instruct mT5
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng indonlp/cendol-mt5-xl 4 &

# ####
# # Zero-Shot 7B Eng
# ####

# # Multilingual - BLOOMZ
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng bigscience/bloomz-7b1 4 &

# # Multilingual - Bactrian-X
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng MBZUAI/bactrian-x-llama-7b-merged 4 &

# # Multilingual - Mistral
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng mistralai/Mistral-7B-Instruct-v0.2 4 &

# # Llama 3
# CUDA_VISIBLE_DEVICES=5 python main_nlu_prompt_batch.py eng meta-llama/Meta-Llama-3-8B-Instruct 4 &

# # English - Falcon
# CUDA_VISIBLE_DEVICES=6 python main_nlu_prompt_batch.py eng tiiuae/falcon-7b-instruct 4 &

# # Bilingual Eng/Chinese - Qwen
# CUDA_VISIBLE_DEVICES=7 python main_nlu_prompt_batch.py eng Qwen/Qwen-7B-Chat 4 &

# # SEA - SEA-LION -- weird error: TypeError: MPTForCausalLM.forward() got an unexpected keyword argument 'token_type_ids'
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng aisingapore/sea-lion-7b-instruct-research 4 &

# # SEA - SeaLLMs
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng SeaLLMs/SeaLLM-7B-v2.5 4 &

# # SEA - SAILOR
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng sail/Sailor-7B-Chat 4 &

# # Indo - Cendol-Instruct LLaMA2
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng indonlp/cendol-llama2-7b 4 &

# # Indo - Merak-7B-v4
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng Ichsan2895/Merak-7B-v4 4 &

# # Vietnamese - PhoGPT
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng vinai/PhoGPT-7B5-Instruct 4 &

# ####
# # Zero-Shot 13B Eng
# ####

# # AYA
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng CohereForAI/aya-101 4 &


# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/mt0-base 16 &
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/mt0-large 8 &
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py ind bigscience/mt0-xl 4 &
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py ind bigscience/mt0-xxl 2 &

# # Zero-Shot BLOOMZ Ind
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloomz-560m 16 &
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b1 12 &
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b7 8 &
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py ind bigscience/bloomz-3b 4 &
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py ind bigscience/bloomz-7b1 2 &

# # Zero-Shot mT0 Eng
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/mt0-small 32 &
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng bigscience/mt0-base 16 &
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng bigscience/mt0-large 8 &
# CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng bigscience/mt0-xl 4 &
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/mt0-xxl 2 &

# # Zero-Shot BLOOMZ Eng
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/bloomz-560m 16 &
# CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng bigscience/bloomz-1b1 12 &
# CUDA_VISIBLE_DEVICES=5 python main_nlu_prompt_batch.py eng bigscience/bloomz-1b7 8 &
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng bigscience/bloomz-3b 4 &
# CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/bloomz-7b1 2 &

# # Zero-Shot Bactrian-X with Bloom 7B Ind
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 20
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 20

# # Zero-Shot Bactrian-X with Bloom 7B Eng
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 20
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 20

# # Zero-Shot aisingapore/sealion7b Ind & Eng
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind aisingapore/sealion7b-instruct-nc 16
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng aisingapore/sealion7b-instruct-nc 16

# # Zero-Shot Merak-V4 Ind
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind Ichsan2895/Merak-7B-v4 8
# CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng Ichsan2895/Merak-7B-v4 8
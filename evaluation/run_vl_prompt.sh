CUDA_VISIBLE_DEVICES=0 python evaluation/main_vl_prompt_batch.py eng google/paligemma-3b-mix-224 1
CUDA_VISIBLE_DEVICES=1 python evaluation/main_vl_prompt_batch.py eng Salesforce/instructblip-vicuna-7b 1
CUDA_VISIBLE_DEVICES=2 python evaluation/main_vl_prompt_batch.py eng llava-hf/llava-1.5-7b-hf 1
CUDA_VISIBLE_DEVICES=3 python evaluation/main_vl_prompt_batch.py eng llava-hf/llava-v1.6-mistral-7b-hf 1
CUDA_VISIBLE_DEVICES=4 python evaluation/main_vl_prompt_batch.py eng HuggingFaceM4/idefics2-8b 1

# Zero-Shot ASR
# 'main_speech_no_prompt_batch.py <prompt_lang> <model_path_or_name> <batch_size> <save_every (OPTIONAL)>'
CUDA_VISIBLE_DEVICES=0 python main_speech_no_prompt_batch.py facebook/wav2vec2-large-xlsr-53 4 &
CUDA_VISIBLE_DEVICES=0 python main_speech_no_prompt_batch.py facebook/wav2vec2-xls-r-2b 4 &

#note: sometimes there is error of CUDA that requires CUDA_LAUNCH_BLOCKING=1, if this occurs, add it to the front of the
#"python" command.
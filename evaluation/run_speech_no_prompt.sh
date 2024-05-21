####
# Zero-Shot ASR
####

# 'main_speech_no_prompt_batch.py <prompt_lang> <model_path_or_name> <batch_size> <save_every (OPTIONAL)>'

####
# Pre-trained
####

# XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py facebook/wav2vec2-large-xlsr-53 8 &

####
# Fine-tuned
####

# English - XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py jonatasgrosman/wav2vec2-large-xlsr-53-english 8 &

# Multilingual - XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py facebook/wav2vec2-xlsr-53-espeak-cv-ft 8 &

# Indonesian - XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py Galuh/wav2vec2-large-xlsr-indonesian 8 &

CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py indonesian-nlp/wav2vec2-indonesian-javanese-sundanese 8 &

# Thai - XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py wannaphong/wav2vec2-large-xlsr-53-th-cv8-newmm 8 &

# Vietnamese - XLSR53 (350M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py nguyenvulebinh/wav2vec2-large-vi-vlsp2020 8 &

# Burmese - XLS-R (300M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py sil-ai/wav2vec2-bloom-speech-mya 8 &

# Khmer - XLS-R (300M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py vitouphy/wav2vec2-xls-r-300m-khmer 8 &

# Tagalog - XLS-R (300M)
CUDA_VISIBLE_DEVICES=1 python main_speech_no_prompt_batch.py sil-ai/wav2vec2-bloom-speech-tgl 8 &

# Note: sometimes there is error of CUDA that requires CUDA_LAUNCH_BLOCKING=1, if this occurs, add it to the front of the "python" command.
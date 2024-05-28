# Zero-Shot ASR
# 'main_speech_wav2vec2_xlsr.py <prompt_lang> <model_path_or_name> <batch_size> <save_every (OPTIONAL)>'
# English - XLSR53 (350M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py jonatasgrosman/wav2vec2-large-xlsr-53-english 4

# Multilingual - XLSR53 (350M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py facebook/wav2vec2-xlsr-53-espeak-cv-ft 4

# Indonesian - XLSR53 (350M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py Galuh/wav2vec2-large-xlsr-indonesian 4
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py indonesian-nlp/wav2vec2-indonesian-javanese-sundanese 4

# Indonesian - Whisper v3 (1.5B)
#cahya/whisper-large-id

# Thai - XLSR53 (350M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py wannaphong/wav2vec2-large-xlsr-53-th-cv8-newmm 4

# Thai - Whisper v3 (1.5B)
#biodatlab/whisper-th-large-v3-combined

# Vietnamese - XLSR53 (350M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py nguyenvulebinh/wav2vec2-large-vi-vlsp2020 4

# Burmese - XLS-R (300M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py sil-ai/wav2vec2-bloom-speech-mya 4

# Khmer - XLS-R (300M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py vitouphy/wav2vec2-xls-r-300m-khmer 4

# Khmer - Whisper v1 (1.5B)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py ksoky/whisper-large-khmer-asr 4

# Tagalog - XLS-R (300M)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_wav2vec2_xlsr.py sil-ai/wav2vec2-bloom-speech-tgl 4

#note: sometimes there is error of CUDA that requires CUDA_LAUNCH_BLOCKING=1, if this occurs, add it to the front of the
#"python" command.

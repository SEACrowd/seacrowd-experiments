# Zero-Shot ASR whisper
# 'main_speech_whisper.py <model_path_or_name> <batch_size> '

# Whisper v3 (1.5B)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_whisper.py openai/whisper-large-v3 16

# Indonesian - Whisper v3
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_whisper.py cahya/whisper-large-id 16

# Thai - Whisper v3 (1.5B)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_whisper.py biodatlab/whisper-th-large-v3-combined 16

# Khmer - Whisper v1 (1.5B)
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_whisper.py  ksoky/whisper-large-khmer-asr 16

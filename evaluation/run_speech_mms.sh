# Zero-Shot ASR mms
# 'main_speech_mms.py <model_path_or_name> <batch_size> '
CUDA_LAUNCH_BLOCKING=1 CUDA_VISIBLE_DEVICES=0 python main_speech_mms.py facebook/mms-1b-all 4 &

#note: sometimes there is error of CUDA that requires CUDA_LAUNCH_BLOCKING=1, if this occurs, add it to the front of the
#"python" command.



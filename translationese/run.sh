# Fine-tuning the translationese classifier

CUDA_VISIBLE_DEVICES=4 python main.py --model_path=microsoft/mdeberta-v3-base --ouput_dir=./runs/ --batch_size=512 --n_epochs=50
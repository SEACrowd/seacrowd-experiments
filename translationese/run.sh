# # Main Exp
# CUDA_VISIBLE_DEVICES=4 python main.py --model_path=FacebookAI/xlm-roberta-base --ouput_dir=./runs/ --batch_size=1024 --n_epochs=50
# CUDA_VISIBLE_DEVICES=4 python main.py --model_path=FacebookAI/xlm-roberta-large --ouput_dir=./runs/ --batch_size=1024 --n_epochs=50
# CUDA_VISIBLE_DEVICES=4 python main.py --model_path=microsoft/mdeberta-v3-base --ouput_dir=./runs/ --batch_size=512 --n_epochs=50
CUDA_VISIBLE_DEVICES=4 python main.py --model_path=sentence-transformers/LaBSE --ouput_dir=./runs/labse --logging_dir=./logs/labse --batch_size=512 --n_epochs=20 --lr 5e-5

# Main Per Lang Exp
# CUDA_VISIBLE_DEVICES=4 python main_per_lang.py --model_path=microsoft/mdeberta-v3-base --ouput_dir=./runs/per_lang_mdeberta-v3-base --batch_size=256 --n_epochs=5

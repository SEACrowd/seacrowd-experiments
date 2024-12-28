# huggingface-cli login --token $HF_TOKEN

# ####
# # Commercial LLMs
# ####

# # OpenAI GPT-4
# python main_nlu_prompt_batch_commercial.py eng openai/gpt-4 8 &

# # Cohere Command-R
# python main_nlu_prompt_batch_commercial.py eng cohere/command-r 8 &

# Cohere Command-R 08-2024
python main_nlu_prompt_batch_commercial.py eng cohere/command-r-08-2024 8

# Cohere Command-R+ 08-2024
python main_nlu_prompt_batch_commercial.py eng cohere/command-r-plus-08-2024 8


# Cohere Command-R7B
python main_nlu_prompt_batch_commercial.py eng cohere/command-r7b-12-2024 0 8

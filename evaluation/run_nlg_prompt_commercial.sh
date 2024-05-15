huggingface-cli login --token $HF_TOKEN

####
# Commercial LLMs
####

# OpenAI GPT-4
python main_nlg_prompt_batch_commercial.py eng openai/gpt-4 0 8 &

# Cohere Command-R
python main_nlg_prompt_batch_commercial.py eng cohere/command-r 0 8 &
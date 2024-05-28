huggingface-cli login --token $HF_TOKEN

####
# Commercial LLMs
####

# OpenAI GPT-4
python main_nlg_prompt_batch_commercial.py openai/gpt-4 8 &

# # Cohere Command-R
# python main_nlg_prompt_batch_commercial.py cohere/command-r 8 &
huggingface-cli login --token $HF_TOKEN

####
# Commercial LLMs
####

# OpenAI GPT-4 BATCH
python main_nlg_prompt_batch_openai_batch.py send_batch eng openai/gpt-4o
# python main_nlg_prompt_batch_openai_batch.py parse_output eng openai/gpt-4o

# OpenAI GPT-4
python main_nlg_prompt_batch_commercial.py eng openai/gpt-4 0 8

# Cohere Command-R
python main_nlg_prompt_batch_commercial.py eng cohere/command-r 0 8 &
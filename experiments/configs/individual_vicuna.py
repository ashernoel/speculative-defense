import os

os.sys.path.append("..")
from configs.template import get_config as default_config

def get_config():
    
    config = default_config()
    print("DEFAULT CONFIG")
    print(config)
    # config.result_prefix = 'results/individual_vicuna'
    config.model_paths = [
        "/n/home10/anoel/vicuna-7b-v1.3/"
    ]
    config.tokenizer_paths = [
        "/n/home10/anoel/vicuna-7b-v1.3/"
    ]
    # config.conversation_templates=['vicuna']

    return config
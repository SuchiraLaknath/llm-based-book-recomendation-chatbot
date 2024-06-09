from ..read_config import Configurations
import json

configs = Configurations().get_config()

def get_available_llm_list():
    llm_list =  configs['llm_models']['available_llms']
    return llm_list
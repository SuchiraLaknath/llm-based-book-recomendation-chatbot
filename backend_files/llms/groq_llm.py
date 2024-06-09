from .base_llm import BaseLlm
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

class LLM(BaseLlm):
    def __init__(self) -> None:
        super().__init__()
    
    def set_llm(self):
        config = self.config['llm_models']['groq']
        self.llm = ChatOpenAI(base_url= config['base_url'] ,api_key= os.environ[config['api_key_name']],temperature = config['temperature'], model=config['model_name'])
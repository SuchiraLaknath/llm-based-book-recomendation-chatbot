from langchain_community.llms.ollama import Ollama
from .base_llm import BaseLlm

class LLM(BaseLlm):
    def __init__(self) -> None:
        super().__init__()
    
    def set_llm(self):
        config = self.config['llm_models']['ollama']
        self.llm = Ollama(model=config['model_name'], temperature= config['temperature'])
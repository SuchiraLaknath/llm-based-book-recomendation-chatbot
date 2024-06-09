from abc import ABC, abstractmethod
from ..read_config import Configurations

class BaseLlm(ABC):
    def __init__(self) -> None:
        self.config =  Configurations().get_config()
        self.set_llm()
    
    @abstractmethod
    def set_llm(self):
        pass
    
    def get_llm(self):
        return self.llm
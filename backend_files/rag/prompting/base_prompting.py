from langchain.prompts import PromptTemplate
from abc import ABC, abstractmethod
import os
from read_config import Configurations

class BasePrompt(ABC):
    def __init__(self) -> None:
        config =  Configurations().get_config()
        system_prompt_path = config['rag']['prompt']['main_search']['system_prompt']
        user_prompt_path = config['rag']['prompt']['main_search']['user_prompt']
        self.system_prompt, self.user_prompt = self.prepare_prompt_texts(system_prompt_file_name= system_prompt_path, user_prompt_file_name= user_prompt_path)
        self.prompt_template = self.prepare_full_prompt_template()

    def prepare_prompt_texts(self, system_prompt_file_name, user_prompt_file_name):
        system_prompt = self.get_prompt(file_path = system_prompt_file_name)
        user_prompt = self.get_prompt(file_path = user_prompt_file_name)
        return system_prompt, user_prompt
    
    @abstractmethod
    def prepare_full_prompt_template(self):
        pass

    def get_full_prompt_text(self, system_prompt, user_prompt):
        prompt_text = self.get_prompt_for_text_for_model(system_prompt=system_prompt, user_prompt= user_prompt)
        return prompt_text
    
    
    def get_prompt(self, file_path):
        prompt_text = self.load_prompt_template_text(file_path)
        return prompt_text

    def load_prompt_template_text(self, template_txt_path):
        f = open(template_txt_path)
        template_txt = f.read()
        f.close()
        return template_txt
    
    def get_system_prompt_template(self):
        return self.system_prompt
    
    def get_user_prompt_template(self):
        return self.user_prompt
    
    def get_prompt_template(self):
        return self.prompt_template
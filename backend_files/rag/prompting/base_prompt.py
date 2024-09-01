from langchain.prompts import PromptTemplate
from abc import ABC, abstractmethod
import os
from read_config import Configurations

class BasePrompt(ABC):
    def __init__(self) -> None:
        self.config =  Configurations().get_config()
        prompt_dir_path = config.prompt_directory_path
        system_prompt_file_name, user_prompt_file_name = config.system_and_human_prompt_files
        self.system_prompt, self.user_prompt = self.prepare_prompt_texts(prompt_dir_path= prompt_dir_path, system_prompt_file_name= system_prompt_file_name, user_prompt_file_name= user_prompt_file_name)
        self.prompt_template = self.prepare_full_prompt_template()

    def prepare_prompt_texts(self, prompt_dir_path, system_prompt_file_name, user_prompt_file_name):
        system_prompt = self.get_prompt(dir_path= prompt_dir_path, file_name= system_prompt_file_name)
        user_prompt = self.get_prompt(dir_path= prompt_dir_path, file_name= user_prompt_file_name)
        return system_prompt, user_prompt
    
    @abstractmethod
    def prepare_full_prompt_template(self):
        pass

    def get_full_prompt_text(self, system_prompt, user_prompt):
        prompt_text = self.get_prompt_for_text_for_model(system_prompt=system_prompt, user_prompt= user_prompt)
        return prompt_text
    
    
    def get_prompt(self, dir_path, file_name):
        file_path = os.path.join(dir_path, file_name)
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
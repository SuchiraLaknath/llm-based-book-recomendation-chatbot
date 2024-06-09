import yaml
import os

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class Configurations:
    
    def __init__(self, file_path = None) -> None:
        if not file_path:
            file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        self.config = self.set_configs(file_path= file_path)
    
    def set_configs(self, file_path):
        config = load_config(file_path= file_path)
        return config
    def get_config(self):
        return self.config
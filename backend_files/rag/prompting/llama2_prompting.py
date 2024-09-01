from langchain.prompts import PromptTemplate
from .base_prompting import BasePrompt

class Prompt(BasePrompt):
    def __init__(self) -> None:
        super().__init__()
    
    def prepare_full_prompt_template(self):
        system_prompt = self.get_system_prompt_template()
        user_prompt = self.get_user_prompt_template()
        template = self.get_full_prompt_text(system_prompt= system_prompt, user_prompt= user_prompt)
        prompt_template = PromptTemplate(
            input_variables=["chat_history", "context", "question"],
            template=template
            )
        return prompt_template
    
    def get_prompt_for_text_for_model(self, system_prompt, user_prompt):
        prompt_text = f"""[INST] <<SYS>>{str(system_prompt)}<</SYS>>
                            {str(user_prompt)}[/INST]"""
        return prompt_text
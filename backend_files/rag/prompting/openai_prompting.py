from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from .base_prompting import BasePrompt

class Prompt(BasePrompt):
    def __init__(self) -> None:
        super().__init__()
    
    def prepare_full_prompt_template(self):
        system_prompt = self.get_system_prompt_template()
        user_prompt = self.get_user_prompt_template()
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", user_prompt),
        ])
        return prompt_template
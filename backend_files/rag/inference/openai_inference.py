from llms.openai_llm import LLM
from .base_inference import BaseInference
from rag.prompting.openai_prompting import Prompt

class Inference(BaseInference):
    def __init__(self) -> None:
        super().__init__()
    
    def get_llm_obj(self):
        return LLM()
    
    def get_prompt_obj(self):
        prompt_obj = Prompt()
        return prompt_obj
    
    # def invoke_llm(self, prompt):
    #     reply = self.llm.invoke(prompt)
    #     return str(reply)
    
    def post_process(self, llm_result):
        post_process_result = llm_result.content
        return post_process_result
from llms.ollma_llm import LLM
from .base_inference import BaseInference
from rag.prompting.llama3_prompting import Prompt

class Inference(BaseInference):
    def __init__(self) -> None:
        super().__init__()
    
    def get_llm_obj(self):
        return LLM()
    
    def get_prompt_obj(self):
        prompt_obj = Prompt()
        return prompt_obj
    
    def post_process(self, llm_result):
        post_process_result = str(llm_result)
        return post_process_result
    
    # def invoke_llm(self, prompt):
    #     reply = str(self.llm.invoke(prompt, stop= ["<|eot_id|>"]))
    #     return reply
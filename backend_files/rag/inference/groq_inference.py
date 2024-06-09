from llms.groq_llm import LLM
from .base_inference import BaseInference

class Inference(BaseInference):
    def __init__(self) -> None:
        super().__init__()
    
    def get_llm_obj(self):
        return LLM()
    
    def post_process(self, llm_result):
        post_process_result = llm_result.content
        return post_process_result
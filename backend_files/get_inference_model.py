import importlib
from  .read_config import Configurations

class GetInferenceModel:
    def __init__(self, llm_name = None) -> None:
        if not llm_name:
            llm_name = Configurations().get_config()['llm_models']['selected_llm']
        self.inference_model = importlib.import_module(name=f".rag.inference.{llm_name}_inference", package="backend_files").Inference()
    
    def get_inference_model(self):
        return self.inference_model
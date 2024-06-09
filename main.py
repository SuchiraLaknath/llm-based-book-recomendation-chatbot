from fastapi import FastAPI
from pydantic import BaseModel, Field
from backend_files.utils.get_available_llms import get_available_llm_list

from backend_files.read_config import Configurations
from backend_files.get_inference_model import GetInferenceModel

inference_model = GetInferenceModel().get_inference_model()

app = FastAPI()

class Prompt_Input(BaseModel):
    user_input : str
    
@app.post("/chat")
def response_to_user_input_text(user_input_text:Prompt_Input):
    user_input = user_input_text.user_input
    return inference_model.get_response(user_input)

@app.get("/get_conversation_history")
def get_chat_history():
    return inference_model.get_conversation_memory()

@app.post('/clear_conversation_history')
def clear_conversation_history():
    inference_model.clear_conversation_history()

@app.get('/get_available_llms')
def get_available_llms():
    return get_available_llm_list()


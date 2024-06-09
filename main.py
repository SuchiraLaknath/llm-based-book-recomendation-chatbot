from fastapi import FastAPI
from pydantic import BaseModel, Field
from backend_files.utils.get_available_llms import get_available_llm_list

from backend_files.read_config import Configurations
from backend_files.get_inference_model import GetInferenceModel

inference_model_obj = GetInferenceModel()

app = FastAPI()

class Prompt_Input(BaseModel):
    user_input : str

class Llm_Name(BaseModel):
    selected_llm_name : str

def get_inference_model(obj):
    return obj.get_inference_model()
    
@app.post("/chat")
def response_to_user_input_text(user_input_text:Prompt_Input):
    user_input = user_input_text.user_input
    inference_model = get_inference_model(obj= inference_model_obj)
    return inference_model.get_response(user_input)

@app.get("/get_conversation_history")
def get_chat_history():
    inference_model = get_inference_model(obj= inference_model_obj)
    return inference_model.get_conversation_memory()

@app.post('/clear_conversation_history')
def clear_conversation_history():
    inference_model = get_inference_model(obj= inference_model_obj)
    inference_model.clear_conversation_history()

@app.post('/select_llm')
def select_llm(llm_name:Llm_Name):
    selected_llm_name = llm_name.selected_llm_name
    if selected_llm_name:
        inference_model_obj.set_inference_model(llm_name=selected_llm_name)
        print(f"--====--- llm_name = {selected_llm_name}")
        return {'selected_llm':selected_llm_name}

@app.get('/get_available_llms')
def get_available_llms():
    return get_available_llm_list()


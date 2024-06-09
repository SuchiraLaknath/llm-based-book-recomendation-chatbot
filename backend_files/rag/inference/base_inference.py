from abc import ABC, abstractmethod
from ..memory.chat_memory_window_buffer import ChatMemory

class BaseInference(ABC):
    def __init__(self) -> None:
        self.llm = self.get_llm()
        self.chat_memory = ChatMemory()
    
    @abstractmethod
    def get_llm_obj(self):
        pass
    
    def get_llm(self):
        llm_obj = self.get_llm_obj()
        return llm_obj.get_llm()
    
    @abstractmethod
    def post_process(self, llm_result):
        pass
    
    def invoke_llm(self, input_prompt):
        llm_result = self.llm.invoke(input_prompt)
        return llm_result
    
    def get_llm_response(self, input_prompt):
        llm_result = self.invoke_llm(input_prompt= input_prompt)
        post_processed_result = self.post_process(llm_result= llm_result)
        return post_processed_result
    
    def get_response(self, user_message):
        result = self.get_llm_response(input_prompt= user_message)
        memory = self.get_conversation_memory()
        memory.chat_memory.add_user_message(user_message)
        memory.chat_memory.add_ai_message(result)
        result_dict = {"result":result}
        return result_dict
    
    def get_conversation_memory(self):
        return self.chat_memory.get_conversation_history()
    
    def clear_conversation_history(self):
        self.chat_memory.clear_conversation_history()
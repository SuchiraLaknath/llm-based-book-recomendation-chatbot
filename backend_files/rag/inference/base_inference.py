from abc import ABC, abstractmethod
from rag.memory.chat_memory_window_buffer import ChatMemory
from rag.context_extractor.extractor import Extractor

class BaseInference(ABC):
    def __init__(self) -> None:
        self.llm = self.get_llm()
        self.chat_memory = ChatMemory()
        self.prompt_obj = self.get_prompt_obj()
        self.extractor_obj = Extractor()
    
    @abstractmethod
    def get_llm_obj(self):
        pass
    
    def get_llm(self):
        llm_obj = self.get_llm_obj()
        return llm_obj.get_llm()
    
    @abstractmethod
    def post_process(self, llm_result):
        pass
    
    @abstractmethod
    def get_prompt_obj(self):
        pass
    
    def get_prompt_template(self):
        return self.prompt_obj.get_prompt_template()
    
    def invoke_llm(self, input_prompt):
        llm_result = self.llm.invoke(input_prompt)
        return llm_result
    
    def get_llm_response(self, input_prompt):
        llm_result = self.invoke_llm(input_prompt= input_prompt)
        print(f"llm result = {llm_result}")
        post_processed_result = self.post_process(llm_result= llm_result)
        return post_processed_result
    
    def prepare_context(self, quary):
        contexts, ids = self.extractor_obj.prepare_context_for_quary(quary = quary)
        return contexts
    
    def get_response(self, user_message):
        contexts = self.prepare_context(quary= user_message)
        memory = self.get_conversation_memory()
        prompt_template = self.get_prompt_template()
        prompt = prompt_template.format(chat_history = memory, context = contexts, question = user_message)
        print("\n*****************************\n context : \n")
        print(prompt)
        result = self.get_llm_response(input_prompt= prompt)
        memory.chat_memory.add_user_message(user_message)
        memory.chat_memory.add_ai_message(result)
        result_dict = {"result":result}
        return result_dict
    
    def get_conversation_memory(self):
        return self.chat_memory.get_conversation_history()
    
    def clear_conversation_history(self):
        self.chat_memory.clear_conversation_history()
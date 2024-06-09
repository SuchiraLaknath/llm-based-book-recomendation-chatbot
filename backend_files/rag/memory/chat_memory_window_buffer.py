from langchain.memory import ConversationBufferWindowMemory
from ...read_config import Configurations

class ChatMemory:
    def __init__(self) -> None:
        self.config = Configurations().get_config()['rag']['chat_memory']
        self.conversation_memory = self.set_conversation_history_memory()
        

    def set_conversation_history_memory(self):
        config = self.config
        memory = ConversationBufferWindowMemory(k= config['window_buffer'])
        return memory
    
    def get_conversation_history(self):
        return self.conversation_memory
    
    def clear_conversation_history(self):
        self.conversation_memory.clear()
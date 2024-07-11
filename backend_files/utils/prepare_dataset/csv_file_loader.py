from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter

class CsvDataLoader:
    def __init__(self, csv_file_path, metadata_columns = [], encoding = "windows-1252", seperator = "\n",  chunk_size = 450, chunk_overlap=0, length_function= len) -> None:
        self.csv_file_path = csv_file_path
        self.encoding = encoding
        self.splitter = self.set_spliter(seperator= seperator, chunk_size= chunk_size, chunk_overlap= chunk_overlap, length_function= length_function)
        self.metadata_columns = metadata_columns
    
    def set_spliter(self, seperator, chunk_size, chunk_overlap, length_function = len):
        splitter = CharacterTextSplitter(separator = seperator,
                                        chunk_size= chunk_size, 
                                        chunk_overlap= chunk_overlap,
                                        length_function= length_function)
        return splitter

    def load_file(self, file_path):
        loader =  CSVLoader(file_path= file_path, encoding= self.encoding, metadata_columns= self.metadata_columns)
        return loader.load()
    
    def split_documents(self, splitter, data):
        return splitter.split_documents(data)
    
    def get_documents(self):
        data = self.load_file(file_path= self.csv_file_path)
        return self.split_documents(splitter= self.splitter,data=data)
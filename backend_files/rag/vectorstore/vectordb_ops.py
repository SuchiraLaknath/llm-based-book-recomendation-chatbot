from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend_files.utils.prepare_dataset.csv_file_loader import CsvDataLoader
from backend_files.read_config import Configurations

class VectorDbOps:

    def __init__(self, create_vector_store = False, configs = None) -> None:
        self.csv_loader_obj, text_embedding_model_name , vectorstore_cache_dir_path = self.get_csvloder_n_embedding_model_name(configs= configs)
        self.text_embedding_model = self.load_huggingface_text_embedding_model(text_embedding_model_name)
        if create_vector_store == True:
            self.vectorstore = self.create_vectorestore(vectorstore_cache_dir=vectorstore_cache_dir_path, embedding_model= self.text_embedding_model)
        else:
            self.vectorstore = self.load_vectorstore_from_cache(vectorstore_cache_dir=vectorstore_cache_dir_path,
                                                  embedding_model= self.text_embedding_model)


    def get_csvloder_n_embedding_model_name(self, configs = None):
        if configs == None:
            configs = Configurations().get_config()
        vectorstore_configs = configs['rag']['vectorstore']
        text_embedding_model_name = vectorstore_configs['embedding_model']
        vectorstore_cache_dir_path = vectorstore_configs['vectordb_cache_directory']
        dataset_file_paths = configs['dataset']
        book_csv_file_path = dataset_file_paths['books_csv']
        csv_loader_config = vectorstore_configs['dataloader']['csv_loader']
        encoding = csv_loader_config['encoding']
        metadata_columns = csv_loader_config['metadata_columns']
        splitter_config = csv_loader_config['splitter']
        seperator = splitter_config['seperator']
        chunk_size = splitter_config['chunk_size']
        chunk_overlap = splitter_config['chunk_overlap']
        csv_loader_obj = CsvDataLoader(csv_file_path= book_csv_file_path, 
                                            seperator= seperator,
                                            metadata_columns= metadata_columns, 
                                            encoding= encoding, 
                                            chunk_size= chunk_size, 
                                            chunk_overlap= chunk_overlap)
        return csv_loader_obj, text_embedding_model_name, vectorstore_cache_dir_path

    def get_documents(self):
        return self.csv_loader_obj.get_documents()
    
    def load_vectorstore_from_cache(self, vectorstore_cache_dir, embedding_model):
        db = Chroma(persist_directory= vectorstore_cache_dir, embedding_function= embedding_model)
        return db
    
    def create_vectorestore(self, vectorstore_cache_dir, embedding_model):
        documents = self.get_documents()
        db = Chroma.from_documents(documents, embedding_model, 
                                   persist_directory= vectorstore_cache_dir)
        db.persist()

    def get_vectorstore(self):
        return self.vectorstore

    def load_huggingface_text_embedding_model(self, model_name):
        embedding_model = HuggingFaceEmbeddings(model_name = model_name)
        return embedding_model
    
    def load_text_embedding_model(self, model_name):
        return self.load_huggingface_text_embedding_model(model_name= model_name)
    
    def get_text_embedding_model(self):
        return self.text_embedding_model
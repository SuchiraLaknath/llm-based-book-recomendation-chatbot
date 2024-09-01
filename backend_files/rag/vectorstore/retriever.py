from .vectordb_ops import VectorDbOps
from read_config import Configurations

class Retriver:
    def __init__(self, configs = None) -> None:
        if configs == None:
            configs = Configurations().get_config()
        vectordb_obj = VectorDbOps(create_vector_store =False)
        self.vector_db = vectordb_obj.get_vectorstore()
        retriever_configs = configs['rag']['vectorstore']['retriever']
        self.k = retriever_configs['retriver_k']
        self.semantic_search_score_threshold = retriever_configs['semantic_search_score_threshold']
        self.search_type = retriever_configs['search_type']

    
    def get_retriever(self, filtered_product_ids = [], max_results = None):
        k = self.k
        score_threshold = self.semantic_search_score_threshold
        search_type = "similarity_score_threshold"
        search_parameters = {"k": k}
        number_of_filtered_docs = len(filtered_product_ids)
        
        if number_of_filtered_docs > 0:
            if self.search_type == "similarity_score_threshold":
                search_parameters["score_threshold"] = score_threshold/2
            search_parameters["filter"] = {'Id_Product':{'$in':filtered_product_ids}}
            search_parameters["k"] = number_of_filtered_docs

        else:
            search_parameters["score_threshold"] = score_threshold
        
        if max_results != None and max_results >0:
            search_parameters["k"] = max_results

           
        return self.vector_db.as_retriever(search_type=search_type, 
                                 search_kwargs=search_parameters)
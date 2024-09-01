from read_config import Configurations
from rag.vectorstore.semantic_search import SemanticSearcher
from rag.no_sql_db.mongodb_ops import Mongo_Ops

class Extractor:
    def __init__(self) -> None:
        self.config = Configurations()
        self.semantic_searcher = SemanticSearcher()
        self.mongo_ops_obj = Mongo_Ops()
        
    def similarity_search_in_vector_database(self, user_quary):
        return self.semantic_searcher.similarity_search_in_vdb(quary=user_quary)

    def no_sql_query(self, product_ids):
        context , filtered_product_ids = self.mongo_ops_obj.get_product_details_for_ids_from_mongodb(product_ids=product_ids)
        return context, filtered_product_ids
        
    def prepare_context_for_quary(self, quary):
        product_ids = self.similarity_search_in_vector_database(user_quary=quary)
        context , filtered_product_ids = self.no_sql_query(product_ids=product_ids)
        # print(f"/n--------------/n ** Context {context}")
        return context, filtered_product_ids
    

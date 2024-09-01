from .retriever import Retriver

class SemanticSearcher:
    
    def __init__(self, configs = None) -> None:
        self.retriver_obj = Retriver(configs= configs)
        
    def get_retriever(self, filtered_product_ids):
        return self.retriver_obj.get_retriever(filtered_product_ids= filtered_product_ids)
    
    def similarity_search_in_vdb(self, quary, filtered_product_ids = []):
        product_ids = []
        retriever = self.get_retriever(filtered_product_ids= filtered_product_ids)
        docs = retriever.invoke(quary)

        for doc in docs:
            # print(doc)
            product_id = doc.metadata["ISBN"]
            product_ids.append(product_id)
 
        print("---------------------------------")
        print(f"number of products ids = {len(product_ids)}")
        return product_ids
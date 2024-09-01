from read_config import Configurations
from pymongo import MongoClient

class Mongo_Ops:
    
    def __init__(self) -> None:
        self.config = Configurations().get_config()
        mongodb_host, mongodb_database_name, mongodb_collection_name = (
                                                self.config['rag']['mongodb']['mongodb_host'], 
                                                self.config['rag']['mongodb']['mongodb_collection_name'], 
                                                self.config['rag']['mongodb']['mongodb_database_name'])
        
        self.mongodb_collection = self.load_mongodb_collection(mongodb_host=mongodb_host, 
                                                               mongodb_database_name=mongodb_database_name, 
                                                               mongodb_collection_name= mongodb_collection_name)

    def load_mongodb_client(self, mongodb_host):
        client = MongoClient(mongodb_host)
        return client
    
    def load_mongodb_db(self, mongodb_host, mongodb_database_name):
        mongo_client = self.load_mongodb_client(mongodb_host= mongodb_host)
        db = mongo_client[mongodb_database_name]
        return db
    
    def load_mongodb_collection(self, mongodb_host, mongodb_database_name, mongodb_collection_name):
        mongodb_db = self.load_mongodb_db(mongodb_host=mongodb_host, mongodb_database_name= mongodb_database_name)
        collection = mongodb_db[mongodb_collection_name]
        return collection
    
    def find_products_by_ids(self, product_ids, limit=None):
        id_list = []
        collection = self.mongodb_collection
        query = {"ISBN": {"$in": product_ids}}
        limit = self.config['rag']['mongodb']['max_mongodb_results']
        products = list(collection.find(query)) 
        for product in products:
            id_list.append(product["ISBN"])      
        if limit is not None:
            products = products[:limit]
            
        return products, id_list
    
    def preprocess_extracted_details_for_single_dict(self, document):
        preporcessed_info = f"""* Book-Title : {document["Book-Title"]}, Author : {document["Book-Author"]}, Publisher: {document["Publisher"]}, Year-Of-Publication: {str(document["Year-Of-Publication"])}, ISBN : {str(document["ISBN"])}"""
        # products_images_n_captions = self.get_product_elements_with_images(document=document)
        return preporcessed_info
    
    def get_product_details_for_ids_from_mongodb(self, product_ids):
        # product_ids = list(map(int, product_ids))
        retrived_documents = str("")

        products_to_chat, filtered_product_ids = self.find_products_by_ids(product_ids= product_ids)
        # print(f"documents = {documents}")
        for document in products_to_chat:
            if document:
                retrived_info = self.preprocess_extracted_details_for_single_dict(document=document)
                retrived_documents = retrived_documents + f"{retrived_info}\n"
            
        return retrived_documents , filtered_product_ids
    
    
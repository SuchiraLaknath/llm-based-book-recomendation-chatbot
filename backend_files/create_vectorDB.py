from rag.vectorstore.vectordb_ops import VectorDbOps

def create_vectordb():
    vectordb_obj = VectorDbOps(create_vector_store =True)
    return vectordb_obj

def main():
    obj = create_vectordb()
    print("VectorDB generation successfull")

if __name__ == "__main__":
    main()
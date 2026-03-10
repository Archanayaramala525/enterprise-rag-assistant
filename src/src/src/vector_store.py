from langchain.vectorstores import FAISS

def create_vector_store(documents, embeddings):
    vector_db = FAISS.from_documents(documents, embeddings)
    return vector_db

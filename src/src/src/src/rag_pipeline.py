from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

def create_rag_chain(vector_db):

    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",
        model_kwargs={"temperature":0.5}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_db.as_retriever()
    )

    return qa_chain

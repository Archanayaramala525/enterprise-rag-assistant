from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Enterprise RAG Assistant API is running"}

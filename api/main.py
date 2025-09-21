from fastapi import FastAPI
from retriever.vector_store import init_db, insert_embeddings, search_similar
from llm.rag_pipeline import rag_answer

app = FastAPI()


@app.on_event("startup")    
def setup():
    init_db()
    insert_embeddings()

@app.get("/ask")
async def ask(query):
    docs = search_similar(query)
    answer = rag_answer(query,docs)
    return {"query": query,  "answer": answer, "sources": [{ "name": d[0], "snippet": d[1] } for d in docs]}

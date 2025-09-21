import json
import os
from sqlalchemy import create_engine,text
from langchain_openai import OpenAIEmbeddings

DB_URL= os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)

# ensure pgvector extension exists
def init_db():
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS hotels_embeddings (
            id SERIAL PRIMARY KEY,
            hotel_id INT,
            name TEXT,
            content TEXT,
            embedding vector(1536)
        )
        """))
def insert_embeddings(file_path="data/hotels.json"):
    embeddings= OpenAIEmbeddings()
    with open(file_path,"r") as f:
        hotels = json.load(f)

    with engine.begin() as conn:
        for h in hotels:
            vector= embeddings.embed_query(h["description"])
            conn.execute(text("""
            INSERT INTO hotels_embeddings (hotel_id, name, content, embedding)
            VALUES (:hotel_id, :name, :content, :embedding)
            """),hotel_id=h["id"],name=h["name"],content=h["description"],embedding=vector)


def search_similar(query,top_k=2):
    embeddings= OpenAIEmbeddings()
    with engine.connect() as conn:
        results = conn.execute(text("""
        SELECT hotel_id, name, content, embedding
        FROM hotels_embeddings
        ORDER BY embedding <-> :query
        LIMIT :top_k
        """),query=embeddings.embed_query(query),top_k=top_k)
        return results.fetchall()



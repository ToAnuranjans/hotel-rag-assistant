import os
from langchain_openai import ChatOpenAI

llm= ChatOpenAI(model="gpt-4o-min", temparature=0)

def rag_answer(query,docs):
    context = "\n".join([f"{d[0]}: {d[1]}" for d in docs])
    prompt = f"""
    You are a hotel assistant. Use the following context to answer the query:
    Context:
    {context}
    Query:{query}
    Answer:
    """
    return llm.invoke(prompt).content
    



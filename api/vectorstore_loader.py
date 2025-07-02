import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def get_vectorstore():
    persist_dir = os.getenv("VECTORDB_PATH")
    emb = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    # will error if not found
    return Chroma(persist_directory=persist_dir, embedding_function=emb)

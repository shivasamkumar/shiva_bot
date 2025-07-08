import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import sys
from pathlib import Path

def get_vectorstore():
    # this will pick up HEROKU config or default to local folder
    rel_path = os.getenv("VECTORDB_PATH", "vector_db")         
    base = Path(__file__).parent.parent                  # /app/api/..
    persist_dir = (base / rel_path).resolve()

    # if we're on Heroku we want to write into /tmp
    if os.getenv("DYNO"):  
        persist_dir = Path("/tmp") / rel_path

    persist_dir.mkdir(parents=True, exist_ok=True)       # ensure it exists

    print(f"[vectorstore_loader] loading embeddings from → {persist_dir}")
    emb = OpenAIEmbeddings()
    return Chroma(persist_directory=str(persist_dir), embedding_function=emb)

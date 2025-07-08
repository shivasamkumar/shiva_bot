import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import sys

def get_vectorstore():
    persist_dir = os.getenv("VECTORDB_PATH", "vector_db")
    print(f"[vectorstore_loader] loading embeddings from → {persist_dir}", file=sys.stderr)
    emb = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vs = Chroma(persist_directory=persist_dir, embedding_function=emb)
    print(f"[vectorstore_loader] found {vs._collection.count()} documents", file=sys.stderr)
    return vs

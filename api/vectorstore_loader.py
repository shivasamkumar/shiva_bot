import os
from pathlib import Path
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma

def get_vectorstore():
    # 1) decide base directory for your persist files
    if os.getenv("DYNO"):  # running on Heroku dyno
        persist_dir = Path("/tmp") / "vector_db"
    else:                  # local run
        base = Path(__file__).parent.parent  # your repo root (/app locally)
        rel  = os.getenv("VECTORDB_PATH", "vector_db")
        persist_dir = (base / rel).resolve()

    # 2) make sure it exists
    persist_dir.mkdir(parents=True, exist_ok=True)

    print(f"[vectorstore_loader] loading embeddings from → {persist_dir}")
    embeddings = OpenAIEmbeddings()
    return Chroma(persist_directory=str(persist_dir), embedding_function=embeddings)

import os
from pathlib import Path
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma

def get_vectorstore():
    if os.getenv("DYNO"):
        # on Heroku, we just copied into /tmp/vector_db
        persist_dir = Path("/tmp") / "vector_db"
    else:
        # local development, point at your committed folder
        base = Path(__file__).parent.parent
        persist_dir = (base / "vector_db").resolve()

    # on Heroku it's already there, and on your machine ingest.py created it,
    # so we don't mkdir here—just load:
    print(f"[vectorstore_loader] opening vectorstore at → {persist_dir}")
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=str(persist_dir),
        embedding_function=embeddings,
    )

import os
import glob
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

MODEL = "gpt-4o-mini"
db_name = "vector_db"

# 1) Load env
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')

# 2) Init your vectorstore (replace with your load code)
KB_ROOT = "../knowledge_base"

# Use utf-8 (or autodetect on Windows)
text_loader_kwargs = {'encoding': 'utf-8'}
# text_loader_kwargs = {'autodetect_encoding': True}

documents = []

# Iterate each folder in the knowledge base
main_folders = glob.glob(os.path.join(KB_ROOT, "*"))
print(main_folders)
for main_folder in main_folders:
    main = os.path.basename(main_folder)  # e.g. "About_Experience"
    print(main)

    # Iterate each keyword subfolder
    keyword_folders = glob.glob(os.path.join(main_folder, "*"))
    for keyword_path in keyword_folders:
        type_ = os.path.basename(keyword_path)  # e.g. "Epics_pro"
        print(type_)

        # Load all .md files under that subfolder
        loader = DirectoryLoader(
            keyword_path,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs=text_loader_kwargs
        )
        folder_docs = loader.load()

        # Tag each document with metadata
        for doc in folder_docs:
            filename = os.path.basename(doc.metadata["source"])
            doc.metadata["doc_type"] = f"{type_}_{filename}"
            doc.metadata["Main"] = main
            doc.metadata["keyword"] = type_
            doc.metadata["filename"] = filename
            documents.append(doc)

print(f"Loaded {len(documents)} markdown documents.")

# Split documents into manageable chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
doc_types = set(chunk.metadata['doc_type'] for chunk in chunks)
print(f"Document types found: {', '.join(doc_types)}")

# Initialize the OpenAI embeddings model
embeddings = OpenAIEmbeddings()

# If a previous vector database exists, delete it to start fresh
if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

# Create a new Chroma vectorstore from the document chunks
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)
print(f"Vectorstore created with {vectorstore._collection.count()} documents")

# Verify the dimensions of one vector (for sanity check)
collection = vectorstore._collection
sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
dimensions = len(sample_embedding)
print(f"The vectors have {dimensions:,} dimensions")
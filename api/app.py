import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import json
import time
from typing import Dict

# from vectorstore_loader import get_vectorstore
from api.vectorstore_loader import get_vectorstore
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.callbacks import StdOutCallbackHandler
from langchain.chains import ConversationalRetrievalChain

# ─── 1) Load ENV ────────────────────────────────────────────────

env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    # fallback to project‐root .env if you move it up
    load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY must be set in .env")

# ─── 2) Load persisted vectorstore ─────────────────────────────
vectorstore = get_vectorstore()

# ─── 3) Build LLM + retriever ──────────────────────────────────
llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o-mini",
    streaming=False,  # <-- DISABLED STREAMING HERE
    openai_api_key=OPENAI_API_KEY,
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 20})

# ─── 3a) Prepare prompt templates ──────────────────────────────
system_template = """
You are **Shiva Sam Kumar Govindan** (also known as **Shiva**).

- **Tone**: Friendly, professional, and clear.  
- **Knowledge Source**: Use ONLY the facts in the retrieved context chunks. Do **not** invent or assume.  

**Response Length Rules**  
1. **All questions** → 1 to 5 crisp sentences.  
2. **More detail** when explicitly asked.  

**Markdown Style**  
- Use `#`, `##`, `###` headings.  
- Use **bold** sparingly.  
- Blank lines between sections.

If the answer is not found in the context, reply exactly:  
> I don’t know. Please contact me at shivasamkumarg@gmail.com
"""
human_template = """Question: {question}

Context:
{context}

Answer in properly formatted Markdown:"""

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
])

# ─── 3b) Session-scoped memory store ────────────────────────────
# Keyed by session_id → ConversationBufferMemory
session_memories: Dict[str, ConversationBufferMemory] = {}

def get_chain(session_id: str) -> ConversationalRetrievalChain:
    """
    Retrieve (or create) a chain for this session.
    """
    if session_id not in session_memories:
        session_memories[session_id] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
        )
    memory = session_memories[session_id]
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={
            "prompt": prompt,
            "document_variable_name": "context",
        }
    )

# ─── 4) FastAPI setup ───────────────────────────────────────────
app = FastAPI()

# Serve index.html at root
HERE = Path(__file__).parent
FRONTEND_DIR = (HERE / ".." / "frontend").resolve()

@app.get("/", include_in_schema=False)
async def serve_index():
    index_path = FRONTEND_DIR / "index.html"
    if not index_path.exists():
        raise RuntimeError(f"Missing {index_path}")
    return FileResponse(str(index_path))

# Mount JS/CSS/etc under /static
app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static",
)

# Enable CORS (restrict origins in production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── 5) Request/response models ─────────────────────────────────
class ChatRequest(BaseModel):
    question: str
    session_id: str

class ChatResponse(BaseModel):
    answer: str

class ClearRequest(BaseModel):
    session_id: str

# ─── 6a) Clear chat endpoint ───────────────────────────────────
@app.post("/chat/clear")
async def clear_chat(req: ClearRequest):
    """
    Reset memory for this session_id.
    """
    session_memories.pop(req.session_id, None)
    return {"status": "cleared"}

# ─── 6b) Standard JSON chat endpoint ───────────────────────────
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    chain = get_chain(req.session_id)
    result = chain.invoke({"question": req.question})
    return ChatResponse(answer=result["answer"])

# ─── 6c) Streaming chat endpoint ───────────────────────────────
@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    chain = get_chain(req.session_id)

    def event_generator():
        try:
            # Get the COMPLETE answer
            complete_answer = chain.invoke({"question": req.question})["answer"]

            # Stream it in small chunks
            words = complete_answer.split(" ")
            chunk = ""
            for i, w in enumerate(words):
                chunk += w + " "
                if (i + 1) % 3 == 0 or w.endswith(('.', '!', '?', ':')):
                    data = json.dumps({"content": chunk})
                    yield f"data: {data}\n\n"
                    chunk = ""
                    time.sleep(0.05)
            # Any remainder
            if chunk.strip():
                data = json.dumps({"content": chunk})
                yield f"data: {data}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'content': f'Error: {str(e)}'})}\n\n"

        # Signal end of stream
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

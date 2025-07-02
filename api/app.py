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

from vectorstore_loader import get_vectorstore
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import ConversationalRetrievalChain

# ─── 1) Load ENV ────────────────────────────────────────────────
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY must be set in .env")

# ─── 2) Load persisted vectorstore ─────────────────────────────
vectorstore = get_vectorstore()

# ─── 3) Build LLM + retrieval chain ────────────────────────────
# DISABLE STREAMING in the LLM
llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o-mini",
    streaming=False,  # <-- DISABLED STREAMING HERE
    openai_api_key=OPENAI_API_KEY,
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
retriever = vectorstore.as_retriever(search_kwargs={"k":20})

system_template = """
You are **Shiva**, a friendly virtual assistant for Shiva Sam Kumar Govindan.
Only answer from the information provided to you, dont assume. 
You don't have to use all the information given to you, be short and to the Point.
Be Short, crisp and Always to the point.cd api  
Be as short as possible.
Reply in clean, well-formatted Markdown.

Use proper markdown formatting:
- Use # ## ### for headers
- Use **text** for bold
- Use normal text for regular content
- Use proper line breaks between sections

If you don't know, say: "I don't know. Please contact me at shivasamkumarg@gmail.com"
"""
human_template = """Question: {question}

Context:
{context}

Answer in properly formatted Markdown:"""

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
])

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={
        "prompt": prompt,
        "document_variable_name": "context",
    },
)

def chat(question: str) -> str:
    """Non-streaming convenience wrapper."""
    return conversation_chain({"question": question})["answer"]

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

class ChatResponse(BaseModel):
    answer: str

# ─── 6a) Standard JSON endpoint ────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    answer = chat(req.question)
    return ChatResponse(answer=answer)

# ─── 6b) FIXED Streaming endpoint - Get complete response first ─────────────────────────────────
@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    def event_generator():
        try:
            # Get the COMPLETE response first (no LLM streaming)
            complete_answer = chat(req.question)
            
            # Now simulate smooth streaming by sending it in chunks
            words = complete_answer.split(' ')
            current_chunk = ""
            
            for i, word in enumerate(words):
                current_chunk += word + " "
                
                # Send chunks every few words or at sentence boundaries
                if (i + 1) % 3 == 0 or word.endswith(('.', '!', '?', ':')):
                    if current_chunk.strip():
                        data = json.dumps({"content": current_chunk})
                        yield f"data: {data}\n\n"
                        current_chunk = ""
                        time.sleep(0.05)  # Small delay for smooth effect
            
            # Send any remaining text
            if current_chunk.strip():
                data = json.dumps({"content": current_chunk})
                yield f"data: {data}\n\n"
                
        except Exception as e:
            error_data = json.dumps({"content": f"Error: {str(e)}"})
            yield f"data: {error_data}\n\n"
        
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
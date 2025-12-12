from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Chatbot SaaS", version="0.1.0")

class ChatRequest(BaseModel):
    client_id: str = Field(min_length=1, max_length=64)
    session_id: str = Field(min_length=1, max_length=128)
    message: str = Field(min_length=1, max_length=2000)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/chat")
def chat(req: ChatRequest):
    # Placeholder: luego se conecta a KB + fallback IA
    return {
        "client_id": req.client_id,
        "session_id": req.session_id,
        "answer": f"Recibí: {req.message}"
    }

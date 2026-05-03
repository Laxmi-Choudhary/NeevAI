from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Optional
import time
from slowapi import Limiter
from slowapi.util import get_remote_address

from services.gemini import get_chat_model
from core.database import get_db

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

class ChatRequest(BaseModel):
    session_id: str = Field(..., min_length=5, max_length=50)
    message: str = Field(..., min_length=1, max_length=500)
    language: Optional[str] = "en"

@router.post("/chat")
@limiter.limit("5/minute")
async def send_chat(request: Request, req: ChatRequest):
    db = get_db()
    collection = db["chat_messages"]
    
    # Store user message
    user_msg = {
        "session_id": req.session_id,
        "role": "user",
        "text": req.message,
        "timestamp": time.time()
    }
    await collection.insert_one(user_msg)
    
    # Retrieve past context (simplified for hackathon: last 10 messages)
    cursor = collection.find({"session_id": req.session_id}).sort("timestamp", 1).limit(10)
    history = await cursor.to_list(length=10)
    
    # Format for Gemini
    contents = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"
        contents.append({"role": role, "parts": [msg["text"]]})
        
    try:
        model = get_chat_model()
        response = model.generate_content(contents)
        reply = response.text
    except Exception as e:
        print(f"Chat Error: {e}")
        reply = "I'm sorry, I'm having trouble processing your request right now. Please try again later."
        
    # Store AI message
    ai_msg = {
        "session_id": req.session_id,
        "role": "model",
        "text": reply,
        "timestamp": time.time()
    }
    await collection.insert_one(ai_msg)
    
    # Strip ObjectId before returning
    ai_msg.pop("_id", None)
    return ai_msg

@router.get("/chat/history")
async def get_chat_history(session_id: str):
    db = get_db()
    collection = db["chat_messages"]
    cursor = collection.find({"session_id": session_id}).sort("timestamp", 1)
    history = await cursor.to_list(length=100)
    
    # Strip _id
    for msg in history:
        msg.pop("_id", None)
        
    return {"history": history}


from typing import Any, Dict

from fastapi import FastAPI
from pydantic import BaseModel

from .chatbot import Chatbot


app = FastAPI(title="AI Shop Assistant")
bot = Chatbot()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest) -> Dict[str, Any]:
    return bot.answer(req.message)


@app.get("/")
def health() -> Dict[str, Any]:
    return {"status": "ok"}


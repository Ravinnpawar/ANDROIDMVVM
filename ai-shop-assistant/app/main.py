import argparse
import json
import os
import sys
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .chatbot import Chatbot
from .database import ProductDatabase


# Singleton instances for API
_db: Optional[ProductDatabase] = None
_bot: Optional[Chatbot] = None


def get_db() -> ProductDatabase:
    global _db
    if _db is None:
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")
        _db = ProductDatabase(data_path)
    return _db


def get_bot() -> Chatbot:
    global _bot
    if _bot is None:
        _bot = Chatbot(get_db())
    return _bot


app = FastAPI(title="AI Shop Assistant", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health() -> Dict[str, Any]:
    return {"status": "ok"}


@app.get("/products")
def search_products(query: str = Query("", description="Search term")) -> Dict[str, Any]:
    db = get_db()
    if not query:
        return {"results": db.list_products()}
    match = db.find_best_match(query)
    if not match:
        return {"results": []}
    return {"results": [match]}


@app.post("/chat")
def chat(req: ChatRequest) -> Dict[str, Any]:
    bot = get_bot()
    reply = bot.handle_message(req.message)
    return {"reply": reply}


def run_cli() -> None:
    print("AI Shop Assistant CLI. Type 'exit' to quit.\n")
    bot = get_bot()
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if user.lower() in {"exit", "quit"}:
            print("Bye!")
            break
        if not user:
            continue
        answer = bot.handle_message(user)
        print(f"Bot: {answer}")


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(description="AI Shop Assistant")
    parser.add_argument("--cli", action="store_true", help="Run interactive CLI")
    args = parser.parse_args(argv)

    if args.cli or os.environ.get("RUN_MODE") == "cli":
        run_cli()
        return 0
    else:
        # If invoked as a module without --cli, print a tip.
        print("Run API with: uvicorn app.main:app --reload", file=sys.stderr)
        print("Run CLI with: python -m app.main --cli", file=sys.stderr)
        run_cli()
        return 0


if __name__ == "__main__":
    raise SystemExit(main())


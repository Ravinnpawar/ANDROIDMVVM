import os
import sys
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from .chatbot import Chatbot


app = typer.Typer(add_completion=False)
console = Console()


@app.command()
def chat(message: Optional[str] = typer.Option(None, "--message", "-m", help="Send a single message and exit.")) -> None:
    """Interactive CLI chat. Press Ctrl+C to exit."""
    bot = Chatbot()

    if message:
        res = bot.answer(message)
        console.print(Panel(res["answer"], title=f"{res['source']} ({res['lang']})"))
        raise typer.Exit(code=0)

    console.print(Panel.fit("AI Shop Assistant — type your question. Ctrl+C to exit."))
    try:
        while True:
            user = console.input("[bold cyan]> [/bold cyan]").strip()
            if not user:
                continue
            res = bot.answer(user)
            console.print(Panel(res["answer"], title=f"{res['source']} ({res['lang']})"))
    except KeyboardInterrupt:
        console.print("\nGoodbye!")


if __name__ == "__main__":
    app()


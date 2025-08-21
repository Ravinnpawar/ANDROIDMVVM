## AI Shop Assistant (POC)

A minimal AI-powered shop assistant that can answer FAQs, look up product prices from a local dataset, and fall back to OpenAI for general questions. Supports English, Hindi, and Marathi responses.

### Features
- FAQ answering: price, delivery, returns, bulk orders
- Product lookup: e.g., "price of raisins"
- AI fallback via OpenAI `gpt-4o-mini`
- Multi-language support (English, Hindi, Marathi)
- CLI and FastAPI web API

### Project Structure
```
ai-shop-assistant/
│── data/
│   └── products.json
│── app/
│   ├── main.py          # FastAPI app + CLI
│   ├── chatbot.py       # core chatbot logic
│   └── database.py      # load products from JSON
│── notebooks/
│   └── demo.ipynb       # interactive demo
│── README.md            # this file
│── requirements.txt     # dependencies
```

### Quickstart

1) Create a virtual environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Set your OpenAI API key (optional but recommended for AI fallback)
```bash
export OPENAI_API_KEY=your_key_here
```

3) Try the CLI
```bash
python -m app.main
```

4) Run the API
```bash
uvicorn app.main:app --reload --port 8000
```

5) Example requests
```bash
# Health
curl -s http://localhost:8000/health

# Product search
curl -s "http://localhost:8000/products?query=raisins"

# Chat
curl -s -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "price of raisins"}'
```

### Why AI?
AI reduces repetitive workload, provides quick multilingual support, and handles queries beyond simple FAQs, improving customer experience and saving time.

### Roadmap
- Web UI (simple chat page)
- Telegram bot integration
- Voice message support
- Inventory and order capture
- Vector search over product catalogs and PDFs

### Notes
- If `OPENAI_API_KEY` is not set, the bot will still function for FAQs and product lookups, but AI fallback will return a friendly default response.


### AI Shop Assistant (POC)

A minimal chatbot that answers customer queries for any shop (retail, farm produce, electronics, etc.).

#### Core Features (MVP)
- **FAQ answering**: price, delivery, return, bulk orders
- **Product lookup**: e.g., "price of raisins" fetched from `data/products.json`
- **AI fallback**: if FAQ/product lookup doesn’t match, uses OpenAI `gpt-4o-mini`
- **Multi-language**: English, Hindi, Marathi — bot replies in the same language
- **Interfaces**: CLI and FastAPI `/chat` endpoint

#### Repo Structure
```
ai-shop-assistant/
│── data/
│   └── products.json
│── app/
│   ├── main.py          # FastAPI app
│   ├── cli.py           # CLI interface
│   ├── chatbot.py       # core chatbot logic
│   └── database.py      # load products from JSON
│── notebooks/
│   └── demo.ipynb       # interactive demo
│── README.md            # this file
│── requirements.txt     # dependencies
```

#### Quickstart
1) Create a virtualenv (optional) and install dependencies
```bash
cd ai-shop-assistant
pip install -r requirements.txt
```

2) (Optional) Set your OpenAI API key for AI fallback
```bash
cp .env.example .env
echo 'OPENAI_API_KEY=your_key_here' >> .env
export OPENAI_API_KEY=your_key_here
```

3) Run the CLI demo
```bash
python -m app.cli
```

4) Run the API (with venv)
```bash
. .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Then call it:
```bash
curl -s -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "price of raisins"}'
```

If `OPENAI_API_KEY` is not set, the app still works using deterministic local responses and product lookup. The AI fallback will degrade gracefully to a standard response.

#### Why AI here?
- Saves time on repetitive customer queries
- Supports multiple languages
- Can scale across different shop types with minimal changes

#### Roadmap
- Voice messages
- Telegram/WhatsApp (Twilio) integrations
- Admin panel to manage products and FAQs
- RAG with embeddings for large catalogs

#### License
MIT


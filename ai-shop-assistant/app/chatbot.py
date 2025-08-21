import os
from typing import Dict, Optional, Tuple

from langdetect import detect
from dotenv import load_dotenv

from .database import ProductDatabase


FAQ_ANSWERS = {
    "delivery": {
        "en": "We deliver within 2-4 days locally. Free delivery over ₹499.",
        "hi": "हम 2-4 दिनों में डिलीवरी करते हैं। ₹499 से ऊपर फ्री डिलीवरी।",
        "mr": "आम्ही 2-4 दिवसांत डिलिव्हरी करतो. ₹499 पेक्षा जास्त मोफत डिलिव्हरी.",
    },
    "returns": {
        "en": "Returns accepted within 7 days with receipt.",
        "hi": "रसीद के साथ 7 दिनों के अंदर रिटर्न स्वीकार है।",
        "mr": "पावतीसोबत 7 दिवसांच्या आत परतावा स्वीकारला जाईल.",
    },
    "bulk": {
        "en": "For bulk orders, discounts are available. Share quantity for a quote.",
        "hi": "थोक ऑर्डर पर छूट उपलब्ध है। मात्रा बताएं, हम कोट भेजेंगे।",
        "mr": "मोठ्या ऑर्डरसाठी सवलत उपलब्ध. प्रमाण सांगा, आम्ही कोट पाठवू.",
    },
    "price": {
        "en": "Please specify the product name to get the latest price.",
        "hi": "कृपया प्रोडक्ट का नाम बताएं ताकि हम कीमत बता सकें।",
        "mr": "कृपया उत्पादनाचे नाव सांगा जेणेकरून आम्ही किंमत सांगू शकू.",
    },
}


def detect_lang(text: str) -> str:
    try:
        code = detect(text)
    except Exception:
        return "en"
    # Map variations to our supported set
    if code.startswith("hi"):
        return "hi"
    if code.startswith("mr"):
        return "mr"
    return "en"


class Chatbot:
    def __init__(self, db: Optional[ProductDatabase] = None) -> None:
        # Load environment variables once for API keys, etc.
        load_dotenv()
        self.db = db or ProductDatabase()
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")

    def answer(self, message: str) -> Dict[str, str]:
        lang = detect_lang(message)

        # 1) Try product lookup for price queries first so it doesn't get shadowed by price FAQ
        price_answer = self._try_product_price(message, lang)
        if price_answer:
            return {"answer": price_answer, "lang": lang, "source": "product_lookup"}

        # 2) Then try simple FAQ intents
        intent, faq_text = self._try_faq(message, lang)
        if faq_text:
            return {"answer": faq_text, "lang": lang, "source": "faq"}

        # 3) Fallback to AI if available
        if self.openai_api_key:
            try:
                ai_text = self._openai_fallback(message, lang)
                if ai_text:
                    return {"answer": ai_text, "lang": lang, "source": "openai"}
            except Exception:
                pass

        # 4) Deterministic fallback
        fallback = {
            "en": "I couldn't find exact info. Could you rephrase or specify the product?",
            "hi": "मुझे सटीक जानकारी नहीं मिली। कृपया फिर से लिखें या प्रोडक्ट बताएं।",
            "mr": "मला अचूक माहिती सापडली नाही. कृपया पुन्हा लिहा किंवा उत्पादन सांगा.",
        }
        return {"answer": fallback.get(lang, fallback["en"]), "lang": lang, "source": "fallback"}

    def _try_faq(self, message: str, lang: str) -> Tuple[Optional[str], Optional[str]]:
        text = message.lower()
        if any(word in text for word in ["deliver", "shipping", "home delivery", "डिलीवरी", "पोच"]):
            return ("delivery", FAQ_ANSWERS["delivery"][lang])
        if any(word in text for word in ["return", "refund", "रिटर्न", "परतावा"]):
            return ("returns", FAQ_ANSWERS["returns"][lang])
        if any(word in text for word in ["bulk", "wholesale", "थोक", "मोठ्या"]):
            return ("bulk", FAQ_ANSWERS["bulk"][lang])
        if any(word in text for word in ["price", "cost", "क़ीमत", "कीमत", "किंमत"]):
            return ("price", FAQ_ANSWERS["price"][lang])
        return (None, None)

    def _try_product_price(self, message: str, lang: str) -> Optional[str]:
        text = message.lower()
        if not any(k in text for k in ["price", "cost", "rate", "कीमत", "क़ीमत", "किंमत"]):
            return None

        # naive extraction: use last token after "of" or whole message
        product_hint = text
        for token in ["price of", "price for", "कीमत ", "किंमत "]:
            if token in text:
                product_hint = text.split(token, 1)[-1].strip()
        product_hint = product_hint.replace("?", "").strip()
        if not product_hint:
            return None

        candidates = self.db.search_by_name(product_hint)
        if not candidates:
            # attempt common plural trim
            if product_hint.endswith("s"):
                candidates = self.db.search_by_name(product_hint[:-1])
        if not candidates:
            return None

        top = candidates[0]
        templates = {
            "en": f"{top['name']}: ₹{top['price']} per {top['unit']}",
            "hi": f"{top['name']}: ₹{top['price']} प्रति {top['unit']}",
            "mr": f"{top['name']}: ₹{top['price']} प्रति {top['unit']}",
        }
        return templates.get(lang, templates["en"])

    def _openai_fallback(self, message: str, lang: str) -> Optional[str]:
        from openai import OpenAI

        client = OpenAI(api_key=self.openai_api_key)
        system_prompt = (
            "You are a concise shop assistant. Answer in the user's language."
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ]
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=180,
        )
        text = completion.choices[0].message.content
        return text


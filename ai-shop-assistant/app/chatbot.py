import os
import re
from typing import Dict, Optional

from langdetect import detect, LangDetectException

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore

from .database import ProductDatabase


LANG_MAP = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
}


FAQ_RESPONSES = {
    "delivery": {
        "en": "We deliver within 2-3 days in the city. Free delivery above ₹999.",
        "hi": "हम शहर में 2-3 दिनों में डिलीवरी करते हैं। ₹999 से ऊपर मुफ्त डिलीवरी।",
        "mr": "आम्ही शहरात २-३ दिवसांत डिलिव्हरी करतो. ₹999 पेक्षा जास्त खरेदीवर मोफत डिलिव्हरी.",
    },
    "returns": {
        "en": "7-day hassle-free returns on unopened items. Keep your bill handy.",
        "hi": "सील बंद सामान के लिए 7-दिन की आसान रिटर्न नीति। बिल संभाल कर रखें।",
        "mr": "सीलबंद वस्तूंवर ७ दिवसांची सोपी रिटर्न पॉलिसी. बिल जपून ठेवा.",
    },
    "bulk": {
        "en": "Bulk discounts available for 10+ units. Share your list for a quote.",
        "hi": "10+ यूनिट्स पर थोक छूट उपलब्ध है। अपना लिस्ट भेजें, हम कोट देंगे।",
        "mr": "१०+ युनिटसाठी घाऊक सूट उपलब्ध. तुमची यादी पाठवा, आम्ही कोट देऊ.",
    },
    "fallback": {
        "en": "I couldn't match that to our FAQs or products. I've noted your query.",
        "hi": "यह प्रश्न हमारे FAQ/प्रोडक्ट्स से मेल नहीं खा सका। मैंने आपका प्रश्न नोट कर लिया है।",
        "mr": "हा प्रश्न आमच्या FAQ/उत्पादनांशी जुळला नाही. मी तुमचा प्रश्न नोंदवला आहे.",
    },
}


PRICE_PATTERNS = [
    re.compile(r"\b(price|rate|cost) of (?P<item>[\w\s]+)", re.IGNORECASE),
    re.compile(r"\b(?P<item>[\w\s]+) (price|rate)$", re.IGNORECASE),
]

DELIVERY_KWS = ["deliver", "delivery", "ship", "shipping", "home delivery"]
RETURN_KWS = ["return", "refund", "exchange"]
BULK_KWS = ["bulk", "wholesale", "stock", "10+", "dozen", "case"]


def detect_language_code(text: str) -> str:
    try:
        code = detect(text)
        if code in LANG_MAP:
            return code
    except LangDetectException:
        pass
    return "en"


class Chatbot:
    def __init__(self, db: ProductDatabase, model: str = "gpt-4o-mini") -> None:
        self.db = db
        self.model = model
        self.client = None
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and OpenAI is not None:
            try:
                self.client = OpenAI()
            except Exception:
                self.client = None

    def _reply_in_language(self, lang: str, text_map: Dict[str, str]) -> str:
        return text_map.get(lang) or text_map.get("en") or ""

    def _match_faq(self, text: str) -> Optional[str]:
        lang = detect_language_code(text)
        lower = text.lower()

        # Delivery
        if any(kw in lower for kw in DELIVERY_KWS):
            return self._reply_in_language(lang, FAQ_RESPONSES["delivery"])

        # Returns
        if any(kw in lower for kw in RETURN_KWS):
            return self._reply_in_language(lang, FAQ_RESPONSES["returns"])

        # Bulk
        if any(kw in lower for kw in BULK_KWS):
            return self._reply_in_language(lang, FAQ_RESPONSES["bulk"])

        # Price via patterns
        for pat in PRICE_PATTERNS:
            m = pat.search(text)
            if m:
                item = m.group("item").strip()
                price_info = self.db.get_price(item)
                if price_info:
                    price, unit, product = price_info
                    name = product.get("name", item)
                    if lang == "hi":
                        return f"{name} की कीमत ₹{price} प्रति {unit} है।"
                    if lang == "mr":
                        return f"{name} ची किंमत ₹{price} प्रति {unit} आहे."
                    return f"{name} costs ₹{price} per {unit}."

        # Loose price lookup by detecting a product token
        # e.g., "raisins price?", "kishmish ka rate?"
        tokens = re.findall(r"[\w]+", lower)
        if tokens:
            candidate = " ".join(tokens[:3])
            price_info = self.db.get_price(candidate)
            if price_info:
                price, unit, product = price_info
                name = product.get("name", candidate)
                if lang == "hi":
                    return f"{name} की कीमत ₹{price} प्रति {unit} है।"
                if lang == "mr":
                    return f"{name} ची किंमत ₹{price} प्रति {unit} आहे."
                return f"{name} costs ₹{price} per {unit}."

        return None

    def _ai_fallback(self, text: str) -> str:
        lang = detect_language_code(text)
        if not self.client:
            return self._reply_in_language(lang, FAQ_RESPONSES["fallback"])

        sys_prompt = (
            "You are a helpful shop assistant. Answer briefly and precisely."
            " Always reply in the user's language."
        )

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": text},
                ],
                temperature=0.3,
                max_tokens=200,
            )
            content = resp.choices[0].message.content.strip()
            return content
        except Exception:
            return self._reply_in_language(lang, FAQ_RESPONSES["fallback"])

    def handle_message(self, text: str) -> str:
        text = (text or "").strip()
        if not text:
            return "Please type a message."

        # First try FAQ + product lookup
        faq = self._match_faq(text)
        if faq:
            return faq

        # Then AI fallback
        return self._ai_fallback(text)


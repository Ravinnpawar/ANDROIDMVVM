import json
import os
import re
from typing import Dict, List, Optional, Tuple


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


class ProductDatabase:
    """Loads and searches products from a JSON file.

    Expected JSON schema (array):
    {
        "id": "raisins",
        "name": "Raisins",
        "synonyms": ["kishmish", "draksha"],
        "unit": "kg",
        "price_inr": 450
    }
    """

    def __init__(self, json_path: str = None) -> None:
        default_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")
        self.json_path = json_path or default_path
        self.products: List[Dict] = []
        self.token_to_product_ids: Dict[str, List[str]] = {}
        self.id_to_product: Dict[str, Dict] = {}
        self._load()

    def _load(self) -> None:
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Products file not found: {self.json_path}")
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)
        self.id_to_product = {p["id"]: p for p in self.products}
        self._build_index()

    def _build_index(self) -> None:
        self.token_to_product_ids.clear()
        for product in self.products:
            product_id = product.get("id")
            names = [product.get("name", ""), product_id]
            names.extend(product.get("synonyms", []) or [])
            for name in names:
                for token in _normalize_text(name).split():
                    if not token:
                        continue
                    self.token_to_product_ids.setdefault(token, []).append(product_id)

    def list_products(self) -> List[Dict]:
        return list(self.products)

    def find_best_match(self, query: str) -> Optional[Dict]:
        """Return the most likely matching product for the query."""
        if not query:
            return None
        q = _normalize_text(query)
        # Exact id or name match
        for product in self.products:
            if q == _normalize_text(product.get("id", "")):
                return product
            if q == _normalize_text(product.get("name", "")):
                return product

        # Token overlap scoring
        tokens = set(q.split())
        product_to_score: Dict[str, int] = {}
        for token in tokens:
            for product_id in self.token_to_product_ids.get(token, []):
                product_to_score[product_id] = product_to_score.get(product_id, 0) + 1

        if not product_to_score:
            # Substring fallback across names and synonyms
            for product in self.products:
                hay = " ".join([
                    product.get("id", ""),
                    product.get("name", ""),
                    " ".join(product.get("synonyms", []) or []),
                ]).lower()
                if q in hay:
                    return product
            return None

        best_product_id = max(product_to_score.items(), key=lambda kv: kv[1])[0]
        return self.id_to_product.get(best_product_id)

    def get_price(self, product_name_or_id: str) -> Optional[Tuple[float, str, Dict]]:
        product = self.find_best_match(product_name_or_id)
        if not product:
            return None
        price = product.get("price_inr")
        unit = product.get("unit", "unit")
        return float(price), unit, product


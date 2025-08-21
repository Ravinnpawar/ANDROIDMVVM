import json
import os
from typing import Any, Dict, List, Optional


class ProductDatabase:
    """Simple product database backed by a JSON file.

    Expects a list of product objects with at least: name, price, unit, category.
    """

    def __init__(self, json_path: Optional[str] = None) -> None:
        self.json_path = json_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "products.json"
        )
        self.products: List[Dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        if not os.path.exists(self.json_path):
            # Seed with a few defaults if file doesn't exist
            os.makedirs(os.path.dirname(self.json_path), exist_ok=True)
            seed = [
                {"name": "Raisins", "price": 320, "unit": "kg", "category": "dry-fruits"},
                {"name": "Almonds", "price": 780, "unit": "kg", "category": "dry-fruits"},
                {"name": "Tomatoes", "price": 30, "unit": "kg", "category": "vegetables"},
                {"name": "Milk 1L", "price": 55, "unit": "pack", "category": "dairy"},
            ]
            with open(self.json_path, "w", encoding="utf-8") as f:
                json.dump(seed, f, ensure_ascii=False, indent=2)

        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                data = data.get("products", [])
            self.products = [self._normalize_product(p) for p in data]

    def _normalize_product(self, p: Dict[str, Any]) -> Dict[str, Any]:
        name = str(p.get("name", "")).strip()
        return {
            "name": name,
            "name_lc": name.lower(),
            "price": p.get("price"),
            "unit": p.get("unit", ""),
            "category": p.get("category", ""),
            "metadata": p.get("metadata", {}),
        }

    def search_by_name(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for p in self.products:
            if q in p["name_lc"]:
                results.append(p)
        return results

    def find_exact(self, name: str) -> Optional[Dict[str, Any]]:
        q = name.lower().strip()
        for p in self.products:
            if p["name_lc"] == q:
                return p
        return None

    def list_categories(self) -> List[str]:
        return sorted({p.get("category", "") for p in self.products if p.get("category")})


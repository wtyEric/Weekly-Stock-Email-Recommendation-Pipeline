import json
import os


def load_stock_ids():
    """Load stock IDs from JSON file"""
    json_path = os.path.join(os.path.dirname(__file__), 'stocks_ID.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

stock_ID = load_stock_ids()
print(stock_ID)
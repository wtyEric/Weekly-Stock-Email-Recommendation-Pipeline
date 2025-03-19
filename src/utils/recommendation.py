import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils import prediction


def load_stock_ids():
    """Load stock IDs from JSON file"""
    json_path = os.path.join(os.path.dirname(__file__), 'stocks_ID.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def get_all_predictions():
    """Get predictions for all stocks in the JSON file"""
    stocks = load_stock_ids()
    predictions = {}
    for name, stock_id in stocks.items():
        try:
            predicted_prices,percentage_change = prediction.stock_prediction(stock_id)
            predictions[name] = {
                'stock_id': stock_id,
                'prediction': predicted_prices,
                'percentage_change': percentage_change
            }
        except Exception as e:
            print(f"Error predicting {name} ({stock_id}): {str(e)}")
            continue
    return predictions

def get_top20_stock_predictions():
    """Get predictions for all stocks in the JSON file and return the top 20 along with HSI data."""
    all_predictions = get_all_predictions()
    # Extract HSI data and remove it from the predictions dictionary
    hsi_data = all_predictions.pop('恒生指數', None)
    # Sort the remaining stocks by percentage_change in descending order
    sorted_stocks = sorted(
        all_predictions.items(),
        key=lambda item: item[1]['percentage_change'],
        reverse=True
    )

    # Take the top 20 entries and convert back to a dictionary
    top20 = {stock[0]: stock[1] for stock in sorted_stocks[:20]}
    print(top20)
    return {
        'HSI': {'恒生指數':hsi_data},
        'top20': top20
    }


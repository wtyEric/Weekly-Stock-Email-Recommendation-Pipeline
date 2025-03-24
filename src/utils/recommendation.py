import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils import prediction


def load_stock_ids(json_name):
    """Load stock IDs from JSON file"""
    json_path = os.path.join(os.path.dirname(__file__), json_name)
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def get_all_predictions():
    """Get predictions for all stocks in the JSON file"""
    stocks = load_stock_ids("stocks_ID.json")
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
    top16_stock = load_stock_ids("top16_stock.json")
    number_of_positive=0
    for stock_name in top16_stock:
        if stock_name in all_predictions and all_predictions[stock_name]['percentage_change'] > 0:
            number_of_positive += 1
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
        'top_weight':f"{number_of_positive} stocks are positive over the top 16 weight stocks in HSI",
        'top20': top20
    }


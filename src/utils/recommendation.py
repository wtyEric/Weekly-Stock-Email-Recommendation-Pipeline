import json
import os
import prediction

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


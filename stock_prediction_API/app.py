from flask import Flask, jsonify
import os, sys
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils.recommendation import get_all_predictions, get_top20_stock_predictions

app = Flask(__name__)

@app.route('/api/predictions', methods=['GET'])
def predictions():
    try:
        predictions = get_all_predictions()
        # Convert NumPy arrays to Python lists
        for stock in predictions.values():
            if isinstance(stock['prediction'], np.ndarray):
                stock['prediction'] = stock['prediction'].tolist()
            if isinstance(stock['percentage_change'], np.float32):
                stock['percentage_change'] = float(stock['percentage_change'])
                
        return jsonify({
            'success': True,
            'data': predictions
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/top20_predictions', methods=['GET'])
def top20_predictions():
    try:
        predictions = get_top20_stock_predictions()
        # Convert NumPy arrays to Python lists
        for stock in predictions['top20'].values():
            if isinstance(stock['prediction'], np.ndarray):
                stock['prediction'] = stock['prediction'].tolist()
            if isinstance(stock['percentage_change'], np.float32):
                stock['percentage_change'] = float(stock['percentage_change'])
        predictions['HSI']["恒生指數"]['prediction'] = predictions['HSI']["恒生指數"]['prediction'].tolist()
        predictions['HSI']["恒生指數"]['percentage_change'] = float(predictions['HSI']["恒生指數"]['percentage_change'])

        return jsonify({
            'success': True,
            'data': predictions
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

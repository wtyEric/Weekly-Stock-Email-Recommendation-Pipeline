from tensorflow.keras.models import load_model
import tensorflow as tf
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.transformation import data_collection
import numpy as np

def sign_accuracy(y_true, y_pred):
    y_true_diff = y_true[:, -1] - y_true[:, 0]
    y_pred_diff = y_pred[:, -1] - y_pred[:, 0]

    y_true_sign = tf.sign(y_true_diff)
    y_pred_sign = tf.sign(y_pred_diff)

    correct_predictions = tf.equal(y_true_sign, y_pred_sign)
    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
    return accuracy

def preparing_prediction_data(ticker_symbol):
        raw_data = data_collection.get_stock_data( ticker_symbol = ticker_symbol, period='6mo')
        raw_data = raw_data.tail(25)
        min_val = raw_data.min()  
        max_val = raw_data.max()  
        data_scaled = ( ((raw_data - min_val))/ (max_val - min_val) ) 
        model_predict_data = np.array(data_scaled)
        return raw_data,model_predict_data[np.newaxis,:],max_val,min_val

def stock_prediction(ticker_symbol):
    raw_data,model_predict_data,max_val, min_val = preparing_prediction_data(ticker_symbol)
    temp_model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'models', f'{ticker_symbol}.h5')
    model = load_model(temp_model_path, custom_objects={'sign_accuracy': sign_accuracy})
    predicted_prices = model.predict(model_predict_data)
    predicted_prices_normal = np.array(((predicted_prices) * (max_val["close"] - min_val["close"]) + min_val["close"])[0])
    percentage_change = (predicted_prices_normal[4] - raw_data["close"].tail(1))/raw_data["close"].tail(1)
    percentage_change =  percentage_change.iloc[0] * 100.0
    return predicted_prices_normal,percentage_change




   
  

    

    
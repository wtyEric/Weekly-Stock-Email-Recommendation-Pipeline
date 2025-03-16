from tensorflow.keras.models import load_model
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.transformation import data_collection
import pandas as pd
import numpy as np

def sign_accuracy(y_true, y_pred):
    import tensorflow as tf
    # Compute change between last and first future prices
    y_true_diff = y_true[:, -1] - y_true[:, 0]
    y_pred_diff = y_pred[:, -1] - y_pred[:, 0]

    # Compute sign of differences
    y_true_sign = tf.sign(y_true_diff)
    y_pred_sign = tf.sign(y_pred_diff)

    # Compare signs
    correct_predictions = tf.equal(y_true_sign, y_pred_sign)
    # Convert booleans to floats and compute mean over batch_size
    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
    return accuracy

def predict_data(ticker_symbol):
        training_data = data_collection.get_stock_data( ticker_symbol = ticker_symbol, period='6mo')
        training_data = training_data.tail(25)
        min_val = training_data.min()  # Min over all features
        max_val = training_data.max()  # Max over all features
        data_scaled = ( ((training_data - min_val))/ (max_val - min_val) ) 
        model_predict_data = np.array(data_scaled)
        return model_predict_data



if __name__ == '__main__':
    temp_model_path = "../../models/^HSI.h5"
    model = load_model(temp_model_path, custom_objects={'sign_accuracy': sign_accuracy})

    

    
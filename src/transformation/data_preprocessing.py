import numpy as np

def create_dataset(data, window_size=10, future_window=5):
    max_index = len(data) - window_size - future_window
    train_data, price = [], []
    for i in range(max_index + 1):
        

        # Get  features
        window = data.iloc[i:(i + window_size)].copy()
        min_val = window.min()  # Min over all features
        max_val = window.max()  # Max over all features

        # min max standardization
        window_scaled = ( ((window - min_val))/ (max_val - min_val) ) 
        train_data.append(window_scaled) 
                        
        future_close_prices = data['close'].iloc[i + window_size  : i + window_size + future_window]
        future_close_prices_scaled = ( (future_close_prices - min_val['close']) / (max_val['close'] - min_val['close']) ) 
        price.append(future_close_prices_scaled) 
        
    return np.array(train_data), np.array(price)
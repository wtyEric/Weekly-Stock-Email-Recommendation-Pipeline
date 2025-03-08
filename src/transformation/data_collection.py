import yfinance as yf
import numpy as np
import ta
import pandas as pd  
def get_stock_data(ticker_symbol, period='20y', interval='1d'):
    # Fetch data for the last 20 years
    data = yf.download(ticker_symbol, period=period, interval=interval)
    columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    predict_data = data[columns].copy()
    predict_data.reset_index(drop=True, inplace=True)

    predict_data.columns = ['open', 'high', 'low', 'close', 'volume']
    df = predict_data
    print(df.shape)
    # Calculate only the required indicators
    df['macd_DIF'] = ta.trend.macd_diff(df['close'])
    df['macd_SIGNAL'] = ta.trend.macd_signal(df['close'])
    df['macd_HIST'] = ta.trend.macd_diff(df['close'])
    df['EMA5'] = ta.trend.ema_indicator(df['close'], window=5)
    df['EMA10'] = ta.trend.ema_indicator(df['close'], window=10)
    df['EMA25'] = ta.trend.ema_indicator(df['close'], window=25)
    df['rsi_14'] = ta.momentum.rsi(df['close'], window=14)
    df['rsi_9'] = ta.momentum.rsi(df['close'], window=9)
    stochastic = ta.momentum.StochasticOscillator(high=df['high'], low=df['low'], close=df['close'], window=14, smooth_window=3)
    df['stoch_%K'] = stochastic.stoch()
    df['stoch_%D'] = stochastic.stoch_signal()
    bb = ta.volatility.BollingerBands(close=df['close'], window=20, window_dev=2)
    df['bb_%b'] = bb.bollinger_pband()  # %B indicator
    df['DMP'] = ta.trend.ADXIndicator(high=df['high'], low=df['low'], close=df['close'], window=14).adx_pos()
    df['ROC'] = ta.momentum.roc(close=df['close'], window=14)
    df['TRIX'] = ta.trend.trix(close=df['close'], window=15)
    df['williams_%R'] = ta.momentum.williams_r(high=df['high'], low=df['low'], close=df['close'], lbp=14)

    
    new_order=['macd_DIF', 'macd_SIGNAL', 'macd_HIST', 'EMA5', 'EMA10', 'EMA25', 'rsi_14', 'rsi_9', 'stoch_%K', 'stoch_%D', 'bb_%b', 'DMP', 'ROC', 'TRIX', 'williams_%R','close']
    df = df[new_order]
    # Return training data starting from index 50 to ensure all indicators have values
    training_data = df.loc[50:]
    return training_data




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

    # Existing indicators
    df['OBV'] = ta.volume.on_balance_volume(df['close'], df['volume'])
    df['macd_DIF'] = ta.trend.macd_diff(df['close'])
    df['macd_SIGNAL'] = ta.trend.macd_signal(df['close'])
    df['macd_HIST'] = ta.trend.macd_diff(df['close'])
    df['EMA5'] = ta.trend.ema_indicator(df['close'], window=5)
    df['EMA10'] = ta.trend.ema_indicator(df['close'], window=10)
    df['EMA25'] = ta.trend.ema_indicator(df['close'], window=25)
    df['rsi_14'] = ta.momentum.rsi(df['close'], window=14)
    df['rsi_9'] = ta.momentum.rsi(df['close'], window=9)
    df['ATR'] = ta.volatility.average_true_range(df['high'], df['low'], df['close'], window=14)

    # New technical indicators (10+ additional features)
    # 1. Stochastic Oscillator
    stochastic = ta.momentum.StochasticOscillator(high=df['high'], low=df['low'], close=df['close'], window=14, smooth_window=3)
    df['stoch_%K'] = stochastic.stoch()
    df['stoch_%D'] = stochastic.stoch_signal()
    
    # 2. Bollinger Bands
    bb = ta.volatility.BollingerBands(close=df['close'], window=20, window_dev=2)
    df['bb_%b'] = bb.bollinger_pband()  # %B indicator
    df['bb_width'] = bb.bollinger_wband()  # Bandwidth
    
    # 3. ADX (Average Directional Movement Index)
    adx_ind = ta.trend.ADXIndicator(high=df['high'], low=df['low'], close=df['close'], window=14)
    df['ADX'] = adx_ind.adx()
    df['DMP'] = adx_ind.adx_pos()  # +DI
    df['DMN'] = adx_ind.adx_neg()  # -DI
    
    # 4. Commodity Channel Index (CCI)
    df['CCI'] = ta.trend.cci(high=df['high'], low=df['low'], close=df['close'], window=20)
    
    # 5. Williams %R
    df['williams_%R'] = ta.momentum.williams_r(high=df['high'], low=df['low'], close=df['close'], lbp=14)
    
    # 6. Chaikin Money Flow (CMF)
    df['CMF'] = ta.volume.chaikin_money_flow(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'], window=20)
    
    # 7. Money Flow Index (MFI)
    df['MFI'] = ta.volume.money_flow_index(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'], window=14)
    
    # 8. Rate of Change (ROC)
    df['ROC'] = ta.momentum.roc(close=df['close'], window=14)
    
    # 9. Parabolic SAR
    df['PSAR'] = ta.trend.psar_up(df['high'], df['low'], df['close'])
    
    # 10. TRIX (Triple Exponential Average)
    df['TRIX'] = ta.trend.trix(close=df['close'], window=15)
    
    # 11. Keltner Channels
    keltner = ta.volatility.KeltnerChannel(high=df['high'], low=df['low'], close=df['close'], window=20, window_atr=10)
    df['keltner_ma'] = keltner.keltner_channel_mband()
    df['keltner_upper'] = keltner.keltner_channel_hband()
    df['keltner_lower'] = keltner.keltner_channel_lband()
    
    # 12. Volume Weighted Average Price (VWAP)
    df['VWAP'] = ta.volume.volume_weighted_average_price(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'], window=20)
    
    # 13. Donchian Channels
    donchian = ta.volatility.DonchianChannel(high=df['high'], low=df['low'], close=df['close'], window=20)
    df['donchian_upper'] = donchian.donchian_channel_hband()
    df['donchian_lower'] = donchian.donchian_channel_lband()
    
    # 14. Standard Deviation
    df['std_dev'] = df['close'].rolling(window=20).std()
    
    # 15. Volume Change Percentage
    df['volume_chg'] = df['volume'].pct_change(periods=5)

    # Return training data starting from index 50 to ensure all indicators have values
    training_data = df.loc[50:]
    return training_data
# Weekly Stock Recommend Pipeline

A data-driven pipeline that generates weekly stock recommendations and sends them via email. This project uses a **CNN + BiLSTM + Self-Attention model** to analyze 20-day historical data and predict 5-day stock trends, recommending the top 5 stocks with the highest percentage gain from the **Hang Seng Index**. The project demonstrates advanced skills in **data engineering**, **machine learning**, and **backend development**.

---

## Features

- **Stock Data Integration**: Automatically fetches historical stock data for the **Hang Seng Index** from APIs .
- **Deep Learning Model**: Implements a CNN + BiLSTM model for time-series forecasting.
- **Recommendation Engine**: Identifies the top 5 stocks with the highest predicted percentage gain.
- **Email Notifications**: Sends weekly stock recommendations to subscribed users.
- **Automated Workflow**: Fully automated pipeline using tools like **Apache Airflow**, **Docker**.
- **Scalable Design**: Designed for scalability and extensibility.

---

## Methodology

### **Approach**

1. **Data Collection**:  
  
   **Extract**:
    - Use APIs from https://www.hsi.com.hk/chi/indexes/all-indexes/hsi to get all HSI's stock_ID.
    - Use APIs from Yahoo Finance to  Fetch the last 20 days of historical stock data for all stocks in the **Hang Seng Index*

    **Transform**:
    -  Data Cleaning: Remove any duplicate entries that may arise during data extraction .Handle missing values by either filling them with the previous day's closing price or removing those records entirely.
    -  Feature Engineering: To use a correlation matrix for feature engineering in The stock prediction model, particularly to identify the best features related to the Hang Seng Index
  
3. **Deep Learning Model**:
    - **CNN + BiLSTM**:
      - **CNN (Convolutional Neural Network)**: Extracts local patterns and features from the 20-day historical data.
      - **BiLSTM (Bidirectional Long Short-Term Memory)**: Captures long-term dependencies and trends in the time series.
    - The model predicts the percentage change for each stock over the next 5 days.

4. **Stock Selection**:
    - Rank all Hang Seng Index stocks by their predicted 5-day percentage gain.
    - Select the **top 5 stocks** with the highest predicted percentage gain.

5. **Email Notifications**:
    - Format the recommendations into an email-friendly template.
    - Send the recommendations to subscribed users.

---

## Pipeline Workflow

1. **Data Collection**:
    - Fetch 20 days of historical stock data for all stocks in the **Hang Seng Index**.
    - Store raw data in cloud storage (e.g., AWS S3).

2. **Data Preprocessing**:
    - Clean and normalize the data using Python and Pandas.
    - Transform the data into a format suitable for the CNN + BiLSTM model.

3. **Model Training**:
    - Train the CNN + BiLSTM model on historical data to predict 5-day stock trends.
    - Save the trained model for reuse.

4. **Prediction & Recommendation**:
    - Use the trained model to predict the 5-day percentage change for each stock in the Hang Seng Index.
    - Select the **top 5 stocks** with the highest predicted percentage gain.

5. **Email Notifications**:
    - Format the stock recommendations into an email-friendly template.
    - Send the recommendations to subscribed users via SMTP.

6. **Automation**:
    - Schedule the entire process to run weekly using Airflow or cron jobs.

---

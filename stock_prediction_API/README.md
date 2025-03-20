# Stock Prediction API

A Flask-based REST API that provides stock price predictions for Hong Kong stocks.

## Prerequisites

- Python 3.x
- Flask
- TensorFlow (for model predictions)
- Other dependencies (listed in requirements.txt)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python app.py
```

2. Access the API endpoint:
- GET `/api/predictions`
  - Returns predictions for all stocks
  - Response format:
```json
{
    "success": true,
    "data": {
        "stock_name": {
            "stock_id": "XXXX.HK",
            "prediction": [...],
            "percentage_change": X.XX
        },
        ...
    }
}
```

## Error Handling

The API returns appropriate error messages in case of failures:
```json
{
    "success": false,
    "error": "Error message"
}
```

## Project Structure

- `app.py` - Main API application
- `models/` - Directory containing trained .h5 model files
- `src/utils/` - Utility functions for predictions and recommendations

## Notes

- The API requires model files (.h5) to be present in the models directory
- Predictions are based on pre-trained machine learning models
- All stock IDs should follow the format XXXX.HK

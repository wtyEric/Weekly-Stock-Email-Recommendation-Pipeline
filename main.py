from src.utils.recommendation import get_top20_stock_predictions
from src.utils.email_stocks import send_stock_recommendation_email
from dotenv import load_dotenv
import os
load_dotenv()


receiver_email = os.getenv("receiver_email")
prediction_result = get_top20_stock_predictions()
send_stock_recommendation_email(prediction_result,receiver_email)



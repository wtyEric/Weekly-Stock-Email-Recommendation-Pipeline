import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
load_dotenv()

# Gmail credentials
sender_email = os.getenv("sender_email")
password = os.getenv("google_app_pw") # Use the 16-digit App Password here




def send_stock_recommendation_email(prediction_result, receiver_email):
    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Weekly Stock Recommendations"

    # Create a user-friendly HTML body
    body = """
    <html>
    <body>
        <h2>Weekly Stock Recommendations</h2>
        <h3>HSI Data</h3>
        <ul>
            <li><strong>恒生指數:</strong></li>
            <ul>
                <li><strong>Stock ID:</strong> {hsi_stock_id}</li>
                <li><strong>Predicted Prices:</strong> {hsi_predicted_prices}</li>
                <li><strong>Percentage Change:</strong> {hsi_percentage_change:.2f}%</li>
            </ul>
        </ul>
        <h3>Top 20 Stock Predictions</h3>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Stock Name</th>
                <th>Stock ID</th>
                <th>Predicted Prices</th>
                <th>Percentage Change</th>
            </tr>
            {stock_rows}
        </table>
    </body>
    </html>
    """

    # Extract HSI data
    hsi_data = prediction_result['HSI']['恒生指數']
    hsi_stock_id = hsi_data['stock_id']
    hsi_predicted_prices = ', '.join(map(str, hsi_data['prediction']))
    hsi_percentage_change = hsi_data['percentage_change']

    # Generate table rows for each stock
    stock_rows = ""
    for stock_name, stock_info in prediction_result['top20'].items():
        predicted_prices = ', '.join(map(str, stock_info['prediction']))
        stock_rows += f"""
        <tr>
            <td>{stock_name}</td>
            <td>{stock_info['stock_id']}</td>
            <td>{predicted_prices}</td>
            <td>{stock_info['percentage_change']:.2f}%</td>
        </tr>
        """

    # Format the body with actual data
    body = body.format(
        hsi_stock_id=hsi_stock_id,
        hsi_predicted_prices=hsi_predicted_prices,
        hsi_percentage_change=hsi_percentage_change,
        stock_rows=stock_rows
    )
    message.attach(MIMEText(body, "html"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


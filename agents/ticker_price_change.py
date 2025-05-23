# agents/ticker_price_change.py
import requests
from datetime import datetime, timedelta

ALPHA_VANTAGE_API_KEY = '87PW7XT9R9YUGI6N'

def get_price_change(ticker, days=1):
    """
    Calculates the percentage price change for a stock over a number of days.

    Args:
        ticker (str): The stock ticker.
        days (int): Number of days in the past to compare.

    Returns:
        str: Description of the price change.
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('Time Series (Daily)', {})
        dates = sorted(data.keys(), reverse=True)
        if len(dates) >= days + 1:
            recent_price = float(data[dates[0]]['4. close'])
            past_price = float(data[dates[days]]['4. close'])
            change = ((recent_price - past_price) / past_price) * 100
            return f"{ticker} changed {change:.2f}% over the past {days} day(s)."
        else:
            return "Insufficient data to calculate price change."
    return "Failed to fetch price history."

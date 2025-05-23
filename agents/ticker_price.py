# agents/ticker_price.py
import requests

ALPHA_VANTAGE_API_KEY = '87PW7XT9R9YUGI6N'

def get_ticker_price(ticker):
    """
    Retrieves the current stock price for the given ticker symbol.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        str: The current stock price or an error message.
    """
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()['Global Quote']
            return f"Current price of {ticker}: ${data['05. price']}"
        except (KeyError, TypeError):
            return "Price data not available."
    else:
        return "Failed to retrieve price."

# agents/ticker_news.py
import requests

ALPHA_VANTAGE_API_KEY = '87PW7XT9R9YUGI6N'  # Replace with your actual API key

def get_ticker_news(ticker):
    """
    Fetches recent news articles for a given stock ticker using Alpha Vantage.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        list: A list of news headlines and summaries.
    """
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            articles = data['feed'][:5]  # Get top 5 articles
            return [f"{article['title']} - {article['summary']}" for article in articles]
        except KeyError:
            return ["No news data available."]
    else:
        return ["Failed to fetch news."]

# agents/ticker_analysis.py
from agents.ticker_news import get_ticker_news
from agents.ticker_price_change import get_price_change

def analyze_ticker(ticker, days=1):
    """
    Combines news and price change data to analyze stock performance.

    Args:
        ticker (str): The stock ticker.
        days (int): Timeframe for price analysis.

    Returns:
        str: Combined analysis report.
    """
    price_info = get_price_change(ticker, days)
    news_items = get_ticker_news(ticker)
    news_summary = "\n".join(news_items)

    return f"Analysis for {ticker} over the past {days} day(s):\n\n{price_info}\n\nRecent News:\n{news_summary}"

# agents/identify_ticker.py

def identify_ticker(user_query):
    """
    Extracts stock ticker symbols from a user query using a predefined mapping.

    Args:
        user_query (str): The user's natural language question.

    Returns:
        str: The ticker symbol if found, otherwise None.
    """
    stock_mapping = {
        "Tesla": "TSLA",
        "Palantir": "PLTR",
        "Nvidia": "NVDA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }

    for company, ticker in stock_mapping.items():
        if company.lower() in user_query.lower():
            return ticker
    return None

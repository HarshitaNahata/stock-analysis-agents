# main_orchestrator.py
from agents.identify_ticker import identify_ticker
from agents.ticker_news import get_ticker_news
from agents.ticker_price import get_ticker_price
from agents.ticker_price_change import get_price_change
from agents.ticker_analysis import analyze_ticker

def handle_query(user_query):
    ticker = identify_ticker(user_query)
    if not ticker:
        return "Sorry, I couldn't identify the stock ticker in your query."

    if "price" in user_query.lower() and "change" not in user_query.lower():
        return get_ticker_price(ticker)

    elif "change" in user_query.lower() or "changed" in user_query.lower():
        days = 7 if "7" in user_query else 1
        return get_price_change(ticker, days)

    elif "why" in user_query.lower() or "happening" in user_query.lower():
        return analyze_ticker(ticker, days=1)

    elif "news" in user_query.lower():
        news = get_ticker_news(ticker)
        return "\n".join(news)

    else:
        return analyze_ticker(ticker)

if __name__ == "__main__":
    print("Welcome to the Stock Analysis System")
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == 'exit':
            break
        response = handle_query(query)
        print("\n" + response + "\n")

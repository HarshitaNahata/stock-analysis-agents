# 🧠 Multi-Agent Stock Analysis System using Google ADK

This project is a modular multi-agent system built to answer stock-related queries using Google ADK and Alpha Vantage API.

## 🚀 Features
- Identify stock ticker from natural language queries
- Retrieve recent news about stocks
- Fetch real-time stock prices
- Analyze price changes over time
- Summarize insights using news + price data

## 📦 Folder Structure
```
stock-analysis-agents/
├── agents/
│   ├── identify_ticker.py
│   ├── ticker_news.py
│   ├── ticker_price.py
│   ├── ticker_price_change.py
│   └── ticker_analysis.py
├── main_orchestrator.py
├── requirements.txt
└── demo_script.txt
```

## 🛠 Requirements
- Python 3.8+
- [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key)

## 🔧 Setup
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/stock-analysis-agents.git
cd stock-analysis-agents

# Install dependencies
pip install -r requirements.txt

# Add your Alpha Vantage API key to all agent files

# Run the system
python main_orchestrator.py
```

## 🧪 Sample Queries
- Why did Tesla stock drop today?
- What’s happening with Palantir stock recently?
- How has Nvidia stock changed in the last 7 days?

## 📽 Demo
See `demo_script.txt` for a video walk-through guide.

## 👨‍🔬 Author
Harshita Nahata

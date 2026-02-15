import pandas as pd
import os
from collector_agent import CollectorAgent
from analyst_agent import AnalystAgent
from dotenv import load_dotenv

load_dotenv()  # loads from .env file
api_key = os.getenv("NEWS_API")

# --- CONFIGURATION ---
STOCK_TICKER = "AAPL"
NEWS_QUERY = "Apple Inc"
API_KEY = api_key

def main():
    print("Starting Financial Sentiment Analysis System...")

    # 1. Initialize Agents
    # Note: If you don't have an API key yet, the collector will warn you.
    collector = CollectorAgent(API_KEY)
    analyst = AnalystAgent()

    # 2. Collect Data
    print(f"\n--- Phase 1: Collection ({STOCK_TICKER}) ---")
    stock_df = collector.get_stock_data(STOCK_TICKER, period="5d")
    news_df = collector.get_financial_news(NEWS_QUERY, days_back=5)

    # 3. Analyze Sentiment (Only if we found news)
    if not news_df.empty:
        print(f"\n--- Phase 2: Analysis ({len(news_df)} articles) ---")
        sentiment_results = analyst.analyze_headlines(news_df['title'].tolist())
        
        # Merge sentiment back into the news dataframe
        news_df['sentiment'] = sentiment_results['sentiment']
        news_df['confidence'] = sentiment_results['confidence']
    else:
        print("No news found to analyze.")

    # 4. Save Results
    print("\n--- Phase 3: Saving Data ---")
    os.makedirs('data', exist_ok=True)
    
    # Save Stock Data
    stock_path = f"data/{STOCK_TICKER}_prices.csv"
    stock_df.to_csv(stock_path, index=False)
    print(f"Saved stock data to {stock_path}")

    # Save News Data
    if not news_df.empty:
        news_path = f"data/{STOCK_TICKER}_sentiment.csv"
        news_df.to_csv(news_path, index=False)
        print(f" Saved sentiment data to {news_path}")
        
        print("\n--- QUICK SUMMARY ---")
        print(news_df['sentiment'].value_counts())

if __name__ == "__main__":
    main()
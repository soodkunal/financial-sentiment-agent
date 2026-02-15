import yfinance as yf
from newsapi import NewsApiClient
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()  # loads from .env file
api_key = os.getenv("NEWS_API")

class CollectorAgent:
    def __init__(self, news_api_key=None):
        # We allow the key to be None for testing stock data only
        if news_api_key:
            self.news_api = NewsApiClient(api_key=news_api_key)
        else:
            self.news_api = None
            print("Warning: No NewsAPI key provided. News functions will fail.")

    def get_stock_data(self, ticker, period="1mo"):
        """
        Fetches historical stock data using yfinance.
        """
        print(f"Collector Agent: Fetching stock data for {ticker}...")
        try:
            stock = yf.Ticker(ticker)
            # We only need the closing price and volume for now
            df = stock.history(period=period)[['Close', 'Volume']]
            df.reset_index(inplace=True)
            # Convert Date to string for easier saving later
            df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
            return df
        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return pd.DataFrame()

    def get_financial_news(self, query, days_back=2):
        """
        Fetches recent news headlines using NewsAPI.
        """
        if not self.news_api:
            print("Error: NewsAPI key not set.")
            return pd.DataFrame()

        print(f"Collector Agent: Searching news for '{query}'...")
        
        # Calculate date range (NewsAPI free tier limits how far back you can go)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        try:
            articles = self.news_api.get_everything(
                q=query,
                from_param=start_date.strftime('%Y-%m-%d'),
                to=end_date.strftime('%Y-%m-%d'),
                language='en',
                sort_by='relevancy',
                page_size=20 # Fetch top 20 relevant articles
            )
            
            news_data = []
            if articles['status'] == 'ok':
                for article in articles['articles']:
                    news_data.append({
                        'date': article['publishedAt'][:10], # Keep just YYYY-MM-DD
                        'title': article['title'],
                        'source': article['source']['name']
                    })
            else:
                print(f"Error: NewsAPI Error: {articles.get('message')}")

            return pd.DataFrame(news_data)

        except Exception as e:
            print(f"Error fetching news: {e}")
            return pd.DataFrame()

# --- TEST BLOCK (Runs only when you run this file directly) ---
if __name__ == "__main__":
    # 1. SETUP: Put your API key here for testing
    MY_API_KEY = api_key

    agent = CollectorAgent(MY_API_KEY)

    # 2. TEST STOCK
    stock_df = agent.get_stock_data("AAPL", period="5d")
    print("\n--- Stock Data Sample ---")
    print(stock_df.head(3))

    # 3. TEST NEWS
    if MY_API_KEY != api_key:
        news_df = agent.get_financial_news("Apple Inc", days_back=1)
        print("\n--- News Data Sample ---")
        print(news_df.head(3))
    else:
        print("\n Skipping News Test: Please paste your API key in the code above.")
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Financial Sentiment Dashboard", layout="wide")

st.title("AI Financial Sentiment Analyst")
st.markdown("Analyzing the correlation between **News Sentiment** and **Stock Price**.")

# --- DATA LOADING ---
@st.cache_data
def load_data(ticker):
    # Load Stock Data
    stock_path = f"data/{ticker}_prices.csv"
    stock_df = pd.read_csv(stock_path)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    
    # Load Sentiment Data
    news_path = f"data/{ticker}_sentiment.csv"
    news_df = pd.read_csv(news_path)
    # Fake a date for news if it doesn't exist (for demo purposes), or use real if available
    if 'date' in news_df.columns:
        news_df['date'] = pd.to_datetime(news_df['date'])
    
    return stock_df, news_df

try:
    # HARDCODED for now - matches your main.py
    TICKER = "AAPL" 
    stock_df, news_df = load_data(TICKER)
    
    # --- METRICS ROW ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        latest_price = stock_df['Close'].iloc[-1]
        st.metric("Latest Stock Price", f"${latest_price:.2f}")
        
    with col2:
        avg_confidence = news_df['confidence'].mean()
        st.metric("Avg. AI Confidence", f"{avg_confidence*100:.1f}%")
        
    with col3:
        sentiment_counts = news_df['sentiment'].value_counts()
        dom_sentiment = sentiment_counts.idxmax()
        st.metric("Dominant Sentiment", dom_sentiment.upper(), 
                 delta=" Bullish" if dom_sentiment == 'positive' else " Bearish")

    # --- CHARTS ---
    
    # 1. Price Chart
    st.subheader(f"{TICKER} Price History")
    fig_price = px.line(stock_df, x='Date', y='Close', title="Closing Price (Last 5 Days)")
    st.plotly_chart(fig_price, use_container_width=True)

    # 2. Sentiment Distribution
    st.subheader("News Sentiment Distribution")
    
    # Create a layout with two columns for charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Pie Chart
        fig_pie = px.pie(news_df, names='sentiment', title="Sentiment Breakdown", 
                         color='sentiment',
                         color_discrete_map={'positive':'green', 'negative':'red', 'neutral':'gray'})
        st.plotly_chart(fig_pie, use_container_width=True)

    with chart_col2:
        # Bar Chart of Confidence
        fig_bar = px.histogram(news_df, x='sentiment', y='confidence', histfunc='avg', 
                               title="Average Confidence by Sentiment",
                               color='sentiment',
                               color_discrete_map={'positive':'green', 'negative':'red', 'neutral':'gray'})
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- RAW DATA TABLE ---
    st.subheader("Recent Analyzed Headlines")
    st.dataframe(news_df[['date', 'title', 'sentiment', 'confidence']], use_container_width=True)

except FileNotFoundError:
    st.error("Data files not found. Please run 'main.py' first to generate data.")
except Exception as e:
    st.error(f"An error occurred: {e}")
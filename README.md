# 📈 Autonomous Financial Sentiment Analyst

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered data pipeline that correlates financial news sentiment with stock price movements. This project leverages **FinBERT** (a Transformer model pre-trained on financial text) to analyze news headlines and visualizes the data using an interactive **Streamlit** dashboard.

---

## 🚀 Key Features

- **Automated Data Collection:** Fetches real-time stock data (via `yfinance`) and financial news (via `NewsAPI`).
- **AI Sentiment Analysis:** Uses `ProsusAI/finbert` to classify headlines as **Positive**, **Negative**, or **Neutral**.
- **Data Aggregation:** Merges unstructured text data with structured stock time-series data.
- **Interactive Dashboard:** Streamlit app to visualize price trends and sentiment distribution.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Machine Learning:** Hugging Face Transformers, PyTorch
- **Data Handling:** Pandas, NumPy
- **APIs:** Yahoo Finance (`yfinance`), NewsAPI
- **Visualization:** Streamlit, Plotly

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/soodkunal/financial-sentiment-agent.git
cd financial-sentiment-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Set Up API Keys

Open:

src/main.py


Replace the placeholder:

NEWS_API_KEY = "your_api_key_here"


⚠️ Recommended: Use environment variables instead of hardcoding your API key.

🏃‍♂️ Usage
Step 1: Run the Data Pipeline
python src/main.py

📊 Output

This will generate:

stock_prices.csv

sentiment_data.csv

inside the data/ folder.

Step 2: Launch the Dashboard
streamlit run src/dashboard.py

📂 Project Structure
financial-sentiment-agent/
├── data/                   # Generated CSV files (ignored by Git)
├── src/
│   ├── analyst_agent.py    # FinBERT sentiment analysis logic
│   ├── collector_agent.py  # Data fetching (NewsAPI + yfinance)
│   ├── dashboard.py        # Streamlit visualization
│   └── main.py             # Orchestrator script
├── requirements.txt
└── README.md

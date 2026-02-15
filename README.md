# 📈 Autonomous Financial Sentiment Analyst

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered data pipeline that correlates financial news sentiment with stock price movements. This project leverages **FinBERT** (a Transformer model pre-trained on financial text) to analyze news headlines and visualizes the data using an interactive **Streamlit** dashboard.

---

## 🚀 Key Features

* **Automated Data Collection:** Fetches real-time stock data (via `yfinance`) and financial news (via `NewsAPI`).
* **AI Sentiment Analysis:** Uses `ProsusAI/finbert` to classify headlines as **Positive**, **Negative**, or **Neutral** with high confidence.
* **Data Aggregation:** Merges unstructured text data with structured time-series stock data.
* **Interactive Dashboard:** A Streamlit app to visualize price trends alongside sentiment distribution.

---

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Machine Learning:** Hugging Face Transformers (`pipeline`), PyTorch
* **Data Handling:** Pandas, NumPy
* **APIs:** Yahoo Finance (`yfinance`), NewsAPI
* **Visualization:** Streamlit, Plotly

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone [https://github.com/soodkunal/financial-sentiment-agent.git](https://github.com/soodkunal/financial-sentiment-agent.git)
cd financial-sentiment-agent

2. Install dependencies
It is recommended to use a virtual environment.

pip install -r requirements.txt

3. Set up API Keys
Get a free API key from NewsAPI.

Open src/main.py.

Replace the placeholder with your actual key:

3. Set up API Keys
Get a free API key from NewsAPI.

Open src/main.py.

Replace the placeholder with your actual key:

🏃‍♂️ Usage
Step 1: Run the Data Pipeline
Execute the main script to fetch data and perform sentiment analysis.

python src/main.py

Output: This will generate stock_prices.csv and sentiment_data.csv in the data/ folder.
'''
### Step 2: Launch the Dashboard
Start the Streamlit app to visualize the results.
'''
streamlit run src/dashboard.py
'''

### 📂 Project Structure
'''
financial-sentiment-agent/
├── data/                   # Stores generated CSV files (ignored by Git)
├── src/
│   ├── analyst_agent.py    # FinBERT sentiment analysis logic
│   ├── collector_agent.py  # Data fetching (NewsAPI + yfinance)
│   ├── dashboard.py        # Streamlit visualization code
│   └── main.py             # Orchestrator script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
'''
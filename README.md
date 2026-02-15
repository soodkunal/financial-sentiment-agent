# 📈 Autonomous Financial Sentiment Analyst

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered data pipeline that correlates financial news sentiment with stock price movements. This project leverages **FinBERT** (a Transformer model pre-trained on financial text) to analyze news headlines and visualizes insights through an interactive **Streamlit** dashboard.

---

## 🌟 Overview

This project demonstrates how modern NLP techniques can be applied to financial analysis by:
- Automatically collecting real-time financial data and news
- Analyzing sentiment using state-of-the-art transformer models
- Correlating sentiment trends with stock price movements
- Visualizing findings through an interactive web dashboard

---

## 🚀 Key Features

- **🤖 Automated Data Collection**
  - Fetches real-time stock data using `yfinance`
  - Retrieves financial news via `NewsAPI`
  - Configurable date ranges and ticker symbols

- **🧠 AI-Powered Sentiment Analysis**
  - Uses `ProsusAI/finbert` for domain-specific financial sentiment classification
  - Classifies headlines as **Positive**, **Negative**, or **Neutral**
  - Provides confidence scores for each prediction

- **📊 Data Aggregation & Processing**
  - Merges unstructured text data with structured time-series stock data
  - Aggregates sentiment scores by day
  - Exports processed data to CSV format

- **📈 Interactive Dashboard**
  - Streamlit-based visualization interface
  - Stock price trends with volume indicators
  - Sentiment distribution charts
  - Correlation analysis between sentiment and price movements

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Machine Learning** | Hugging Face Transformers, PyTorch |
| **Data Processing** | Pandas, NumPy |
| **APIs** | Yahoo Finance (`yfinance`), NewsAPI |
| **Visualization** | Streamlit, Plotly |
| **Models** | FinBERT (ProsusAI/finbert) |

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or higher installed
- A NewsAPI key (get one free at [newsapi.org](https://newsapi.org))
- Basic understanding of Python and command line
- Git installed on your system

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/soodkunal/financial-sentiment-agent.git
cd financial-sentiment-agent
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

**Option 1: Environment Variables (Recommended)**

Create a `.env` file in the project root:

```bash
NEWS_API_KEY=your_newsapi_key_here
```

Then update `src/main.py` to load from environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
```

**Option 2: Direct Configuration**

Open `src/main.py` and replace the placeholder:

```python
NEWS_API_KEY = "your_api_key_here"
```

> ⚠️ **Security Note:** Never commit API keys to version control. Add `.env` to your `.gitignore` file.

---

## 🏃‍♂️ Usage

### Quick Start

1. **Run the Data Pipeline**

```bash
python src/main.py
```

This script will:
- Fetch stock price data for the configured ticker symbol
- Retrieve recent financial news articles
- Analyze sentiment using FinBERT
- Generate CSV files in the `data/` directory

**Expected Output:**
```
✓ Stock prices saved to data/stock_prices.csv
✓ Sentiment analysis saved to data/sentiment_data.csv
```

2. **Launch the Interactive Dashboard**

```bash
streamlit run src/dashboard.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### Configuration

You can customize the analysis by modifying parameters in `src/main.py`:

```python
# Example configuration
TICKER = "AAPL"           # Stock ticker symbol
START_DATE = "2024-01-01" # Analysis start date
END_DATE = "2024-02-15"   # Analysis end date
NEWS_QUERY = "Apple Inc"  # News search query
```

---

## 📂 Project Structure

```
financial-sentiment-agent/
│
├── data/                       # Generated data files (git-ignored)
│   ├── stock_prices.csv       # Historical stock price data
│   └── sentiment_data.csv     # Analyzed news sentiment data
│
├── src/                       # Source code
│   ├── analyst_agent.py      # FinBERT sentiment analysis module
│   ├── collector_agent.py    # Data collection (NewsAPI + yfinance)
│   ├── dashboard.py          # Streamlit visualization dashboard
│   └── main.py               # Main orchestrator script
│
├── .env                       # Environment variables (create this)
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## 📊 Output Files

### `data/stock_prices.csv`

Contains historical stock price data:

| Column | Description |
|--------|-------------|
| Date | Trading date |
| Open | Opening price |
| High | Highest price |
| Low | Lowest price |
| Close | Closing price |
| Volume | Trading volume |

### `data/sentiment_data.csv`

Contains sentiment analysis results:

| Column | Description |
|--------|-------------|
| Date | Publication date |
| Headline | News headline text |
| Sentiment | Positive/Negative/Neutral |
| Score | Confidence score (0-1) |

---

## 🔍 How It Works

1. **Data Collection**
   - `collector_agent.py` fetches stock prices from Yahoo Finance
   - Retrieves financial news articles from NewsAPI based on keywords

2. **Sentiment Analysis**
   - `analyst_agent.py` uses FinBERT to analyze each headline
   - Assigns sentiment labels with confidence scores
   - Aggregates results by date

3. **Visualization**
   - `dashboard.py` loads the processed data
   - Creates interactive charts showing price trends and sentiment
   - Displays correlation metrics

4. **Orchestration**
   - `main.py` coordinates the entire pipeline
   - Handles error logging and data export

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Check code style
flake8 src/
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FinBERT Model:** [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert)
- **NewsAPI:** [newsapi.org](https://newsapi.org)
- **yfinance:** Yahoo Finance market data downloader
- **Streamlit:** Interactive dashboard framework

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'transformers'`
- **Solution:** Ensure you've activated your virtual environment and run `pip install -r requirements.txt`

**Issue:** `API key invalid`
- **Solution:** Verify your NewsAPI key is correct and has not expired

**Issue:** `No data found for ticker symbol`
- **Solution:** Check that the ticker symbol is valid and the date range includes trading days

**Issue:** Dashboard not loading
- **Solution:** Ensure the CSV files exist in the `data/` directory by running `src/main.py` first

---


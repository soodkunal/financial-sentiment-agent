from transformers import pipeline
import pandas as pd

class AnalystAgent:
    def __init__(self):
        print("Analyst Agent: Loading FinBERT model... (This will download ~400MB the first time)")
        # We use a specific model trained on financial data, not generic English
        self.sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")

    def analyze_headlines(self, headlines):
        """
        Input: A list of headlines (strings)
        Output: A DataFrame with original text, sentiment label, and confidence score
        """
        print(f" Analyst Agent: Analyzing {len(headlines)} headlines...")
        
        # The pipeline returns a list of dicts: [{'label': 'positive', 'score': 0.95}, ...]
        results = self.sentiment_pipeline(headlines)
        
        # Combine input and output into a structured table
        df = pd.DataFrame({
            'headline': headlines,
            'sentiment': [r['label'] for r in results],
            'confidence': [r['score'] for r in results]
        })
        
        return df

# --- TEST BLOCK ---
if __name__ == "__main__":
    # Simple test to ensure the model loads correctly
    agent = AnalystAgent()
    test_data = ["Stocks are soaring!", "Inflation is destroying the market."]
    print(agent.analyze_headlines(test_data))
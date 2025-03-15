import requests
from textblob import TextBlob

API_KEY = "63ab31f97bc040258efb52f06e65****"

# Fetch news from NewsAPI
def get_financial_news():
    url = f"https://newsapi.org/v2/top-headlines?sources=bloomberg,reuters&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        return [
            {
                "title": article["title"],
                "url": article["url"],
                "sentiment": analyze_sentiment(article["title"]),
            }
            for article in news_data["articles"]
        ]
    else:
        return {"error": f"Failed to fetch news. Status Code: {response.status_code}"}

# AI Sentiment Analysis Function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Value between -1 and 1

    if polarity > 0:
        return "Positive 😀 (Bullish)"
    elif polarity < 0:
        return "Negative 😟 (Bearish)"
    else:
        return "Neutral 😐"

# Test the function
if __name__ == "__main__":
    print("Financial News Sentiment:", get_financial_news())

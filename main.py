from fastapi import FastAPI
from news_api import get_financial_news

app = FastAPI()

# API Endpoint: Get financial news with AI sentiment analysis
@app.get("/news/sentiment")
def financial_news_sentiment():
    return {"news": get_financial_news()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

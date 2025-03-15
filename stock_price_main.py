from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/market-data/stocks")
def get_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=YOUR_ALPHA_VANTAGE_KEY"
    response = requests.get(url).json()
    return {"stock_data": response}

@app.get("/market-data/crypto")
def get_crypto_data(symbol: str):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url).json()
    return {"crypto_price": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

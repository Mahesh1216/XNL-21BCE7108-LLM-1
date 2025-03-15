import time
import pandas as pd
import numpy as np
import ta
from binance.client import Client
from llm_sentiment import analyze_sentiment 
from database import log_trade

# Binance API Keys 
API_KEY = "jr5TIUAfl9O2yNnIS6HygA28dntIkY5vDjousUv3cw9eu3a8xZ4nwrjtX********"
API_SECRET = "jnfxQ9z33dINkFcaVEG1i14A2QTEkkt278X91xxFwGHnurUu**********"

client = Client(API_KEY, API_SECRET, tld='com')

def get_crypto_price(symbol="BTCUSDT"):
    ticker = client.get_ticker(symbol=symbol)
    return float(ticker["lastPrice"])

#Function to Execute a Trade
def execute_trade(symbol, trade_type, quantity, ai_decision, tech_decision, sentiment):
    price = get_crypto_price(symbol)
    try:
        if trade_type == "BUY":
            order = client.order_market_buy(symbol=symbol, quantity=quantity)
        elif trade_type == "SELL":
            order = client.order_market_sell(symbol=symbol, quantity=quantity)
        
        print(f"✅ Trade Executed: {trade_type} {quantity} {symbol} at ${price}")

        log_trade(symbol, trade_type, price, quantity, sentiment, ai_decision, tech_decision)

    except Exception as e:
        print(f"⚠️ Trade Execution Failed: {e}")
def ai_technical_trading(symbol="BTCUSDT", quantity=0.001):

    latest_news = "Bitcoin price surges after major institutional investment."
    sentiment_result = analyze_sentiment(latest_news)
    sentiment_label = sentiment_result["label"]
    ai_decision = "HOLD"
    if sentiment_label == "POSITIVE":
        ai_decision = "BUY"
    elif sentiment_label == "NEGATIVE":
        ai_decision = "SELL"

    # Fetch Market Data for Technical Indicators
    df = pd.DataFrame(client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=50),
                      columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time',
                               'Quote_asset_volume', 'Number_of_trades', 'Taker_buy_base', 'Taker_buy_quote', 'Ignore'])
    df['Close'] = df['Close'].astype(float)
    
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    bb = ta.volatility.BollingerBands(df['Close'], window=20, window_dev=2)
    df['BB_upper'] = bb.bollinger_hband()
    df['BB_lower'] = bb.bollinger_lband()
    df['MACD'] = ta.trend.MACD(df['Close']).macd()

    latest = df.iloc[-1]
    current_price = latest['Close']

    # Technical Indicator Decision
    tech_decision = "HOLD"
    if latest['RSI'] < 30 and current_price < latest['BB_lower']:
        tech_decision = "BUY"
    elif latest['RSI'] > 70 and current_price > latest['BB_upper']:
        tech_decision = "SELL"

    print(f"\n🔹 AI Sentiment: {sentiment_label}")
    print(f"📈 Price: {current_price} | RSI: {latest['RSI']:.2f} | MACD: {latest['MACD']:.2f}")
    print(f"📊 AI Decision: {ai_decision} | 📊 Technical Decision: {tech_decision}")

    # Final Trade Execution (Only When AI + Technical Match)
    if ai_decision == "BUY" and tech_decision == "BUY":
        execute_trade(symbol, "BUY", quantity, ai_decision, tech_decision, sentiment_label)
    elif ai_decision == "SELL" and tech_decision == "SELL":
        execute_trade(symbol, "SELL", quantity, ai_decision, tech_decision, sentiment_label)
    else:
        print("⏳ Holding position... Waiting for AI and Technical Indicators to align.")

# Run Trading Bot (Loop Every 60s)
if __name__ == "__main__":
    while True:
        ai_technical_trading("BTCUSDT", 0.001)
        time.sleep(3)  # Runs every 3 seconds


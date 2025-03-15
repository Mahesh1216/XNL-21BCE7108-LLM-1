import pandas as pd
import pandas_ta as ta
import yfinance as yf

# Fetch test data
data = yf.download("BTC-USD", start="2022-01-01", end="2024-01-01")

# Ensure 'Close' column exists
if "Close" not in data.columns:
    raise ValueError("Error: 'Close' column is missing from Yahoo Finance data.")

# Calculate MACD
macd = ta.macd(data["Close"], fast=12, slow=26, signal=9)

print(macd)

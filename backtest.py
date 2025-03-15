import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock/crypto price data
def get_historical_data(symbol="BTC-USD", start="2022-01-01", end="2024-01-01"):
    data = yf.download(symbol, start=start, end=end)

    rename_dict = {
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Adj Close": "Adj_Close",
        "Volume": "Volume"
    }
    data.rename(columns=rename_dict, inplace=True)

    #Drop missing values
    data.dropna(inplace=True)
    
    return data

def vectorized_backtest(data, short_window=20, long_window=50, initial_cash=10000):
    # Compute Moving Averages
    data["Short_MA"] = data["Close"].rolling(window=short_window).mean()
    data["Long_MA"] = data["Close"].rolling(window=long_window).mean()

    data["Signal"] = 0  # Default: Hold
    data.loc[data["Short_MA"] > data["Long_MA"], "Signal"] = 1  # Buy Signal
    data.loc[data["Short_MA"] < data["Long_MA"], "Signal"] = -1  # Sell Signal

    data["Position"] = data["Signal"].shift(1)  
    
    # Fill NaN values in Position with 0
    data["Position"] = data["Position"].fillna(0)
    data["Price_Change"] = data["Close"].pct_change()    
    data["Daily_Return"] = data["Position"] * data["Price_Change"]

    data["Cumulative_Return"] = (1 + data["Daily_Return"].fillna(0)).cumprod() * initial_cash
    return data

def run_backtest(symbol="BTC-USD"):
    data = get_historical_data(symbol)

    if data.empty:
        print("⚠️ No data available for backtesting.")
        return

    results = vectorized_backtest(data)

    plt.figure(figsize=(12, 6))
    plt.plot(results.index, results["Cumulative_Return"], label="Strategy Performance", color="blue")
    plt.title(f"Backtest Results for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid()
    plt.show()

    final_value = results["Cumulative_Return"].iloc[-1]
    print(f"📊 Final Portfolio Value: ${final_value:.2f}")

if __name__ == "__main__":
    run_backtest("BTC-USD")
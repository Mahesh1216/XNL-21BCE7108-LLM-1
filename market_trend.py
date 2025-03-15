import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
# Fetch historical stock data
def get_stock_data(symbol="AAPL", start="2023-01-01", end="2024-01-01"):
    stock = yf.download(symbol, start=start, end=end)
    return stock
from statsmodels.tsa.arima.model import ARIMA

# Train ARIMA Model & Predict Future Prices
def predict_stock_trend(symbol="AAPL"):
    stock_data = get_stock_data(symbol)
    close_prices = stock_data["Close"]

    # Train ARIMA Model
    model = ARIMA(close_prices, order=(5, 1, 0))  # (p, d, q) → Adjust for better results
    model_fit = model.fit()

    # Predict next 30 days
    future_steps = 30
    forecast = model_fit.forecast(steps=future_steps)

    plt.figure(figsize=(10, 5))
    plt.plot(close_prices, label="Historical Prices")
    plt.plot(pd.date_range(close_prices.index[-1], periods=future_steps, freq="B"), forecast, label="Predicted Prices", linestyle="dashed")
    plt.legend()
    plt.title(f"{symbol} Stock Price Prediction (ARIMA)")
    plt.show()

if __name__ == "__main__":
    predict_stock_trend("AAPL")  # Predict Apple Stock Prices



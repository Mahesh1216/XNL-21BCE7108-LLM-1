import numpy as np
import pandas as pd

# Risk Assessment Agent
def calculate_risk(stock_data):
    """
    Uses standard deviation (volatility) & Value at Risk (VaR) to assess risk.
    """
    returns = stock_data['Close'].pct_change().dropna()
    volatility = np.std(returns)
    VaR = np.percentile(returns, 5)  # 5% worst-case loss

    return {"volatility": volatility, "Value_at_Risk": VaR}

# Fraud Detection Agent 
def detect_fraudulent_activity(trades):
    """
    Checks for irregular transactions & suspicious trades.
    """
    unusual_trades = [trade for trade in trades if trade['quantity'] > 10]  # Example threshold
    return unusual_trades

# Portfolio Manager Agent (Simplified)
def portfolio_optimization(stock_data):
    """
    Uses Sharpe Ratio to optimize investment portfolio.
    """
    returns = stock_data['Close'].pct_change().dropna()
    risk_free_rate = 0.02  #risk-free rate
    sharpe_ratio = (np.mean(returns) - risk_free_rate) / np.std(returns)

    return {"sharpe_ratio": sharpe_ratio, "investment_decision": "BUY" if sharpe_ratio > 1 else "SELL"}

# sample Test Execution
if __name__ == "__main__":
    stock_data = pd.DataFrame({
        "Close": [100, 102, 101, 105, 110, 120, 115, 117, 125, 130]
    })
    trades = [
        {"quantity": 5, "price": 100},
        {"quantity": 15, "price": 105},  # Suspicious trade
        {"quantity": 2, "price": 110}
    ]
    risk_result = calculate_risk(stock_data)
    fraud_result = detect_fraudulent_activity(trades)
    portfolio_result = portfolio_optimization(stock_data)

    print("\n📊 Risk Assessment Result:")
    print(risk_result)

    print("\n🕵️ Fraud Detection Result:")
    print(fraud_result)

    print("\n📈 Portfolio Optimization Result:")
    print(portfolio_result)

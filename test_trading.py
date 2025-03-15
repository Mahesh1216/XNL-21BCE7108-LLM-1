import pytest
from unittest.mock import patch
from tradebot import ai_technical_trading, execute_trade

# ✅ Mock Binance API
@patch("tradebot.get_crypto_price", return_value=60000)
@patch("tradebot.analyze_sentiment", return_value=[{"label": "POSITIVE"}])
def ai_technical_trading(mock_price, mock_sentiment):
    decision = ai_technical_trading("BTCUSDT", 0.001)
    assert decision in ["BUY", "SELL", "HOLD"], "Invalid trade decision!"

# ✅ Mock Trade Execution (Prevents real trades)
@patch("tradebot.client.order_market_buy")
@patch("tradebot.client.order_market_sell")
def test_execute_trade(mock_buy, mock_sell):
    execute_trade("BTCUSDT", "BUY", 0.001)
    mock_buy.assert_called_once()

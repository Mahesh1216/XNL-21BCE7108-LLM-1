from database import get_trade_history

# ✅ Fetch and Display Trade History
trades = get_trade_history()

if trades:
    print("📊 Trade History:")
    for trade in trades:
        print(trade)
else:
    print("⚠️ No trades found in database.")

import sqlite3

# ✅ Connect to SQLite Database (Creates if it doesn’t exist)
conn = sqlite3.connect("trading_history.db")
cursor = conn.cursor()

# ✅ Create Trade History Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    symbol TEXT,
    trade_type TEXT,
    price REAL,
    quantity REAL,
    sentiment TEXT,
    ai_decision TEXT,
    technical_decision TEXT
)
''')
conn.commit()

# ✅ Print confirmation message
print("✅ Database initialized successfully: 'trading_history.db'")

# ✅ Function to Log a Trade
def log_trade(symbol, trade_type, price, quantity, sentiment, ai_decision, technical_decision):
    cursor.execute('''
        INSERT INTO trades (timestamp, symbol, trade_type, price, quantity, sentiment, ai_decision, technical_decision)
        VALUES (datetime('now'), ?, ?, ?, ?, ?, ?, ?)
    ''', (symbol, trade_type, price, quantity, sentiment, ai_decision, technical_decision))
    conn.commit()
    print("✅ Trade Logged in Database")

# ✅ Function to Fetch All Trades
def get_trade_history():
    cursor.execute("SELECT * FROM trades")
    return cursor.fetchall()

if __name__ == "__main__":
    print("✅ Database setup complete! Run `tradebot.py` to log trades.")

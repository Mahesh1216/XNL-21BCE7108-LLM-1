from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "12345678"

class FraudDetection:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def log_trade(self, trade_id, trader, symbol, trade_type, price, quantity):
        with self.driver.session() as session:
            session.write_transaction(self._create_trade, trade_id, trader, symbol, trade_type, price, quantity)

    @staticmethod
    def _create_trade(tx, trade_id, trader, symbol, trade_type, price, quantity):
        query = """
        MERGE (t:Trader {name: $trader})
        CREATE (tr:Trade {trade_id: $trade_id, symbol: $symbol, trade_type: $trade_type, price: $price, quantity: $quantity})
        MERGE (t)-[:EXECUTED]->(tr)
        """
        tx.run(query, trade_id=trade_id, trader=trader, symbol=symbol, trade_type=trade_type, price=price, quantity=quantity)

    def detect_fraud(self):
        with self.driver.session() as session:
            return session.read_transaction(self._detect_anomalies)

    @staticmethod
    def _detect_anomalies(tx):
        query = """
        MATCH (t:Trader)-[:EXECUTED]->(tr:Trade)
        WHERE tr.quantity > 10  // Example rule: Large trades are suspicious
        RETURN t.name AS Trader, tr.symbol AS Symbol, tr.quantity AS Quantity, tr.price AS Price, tr.trade_type AS Type
        """
        result = tx.run(query)
        return [record for record in result]

if __name__ == "__main__":
    fraud_system = FraudDetection()


    fraud_system.log_trade(1, "Trader_A", "BTCUSDT", "BUY", 65000, 0.5)
    fraud_system.log_trade(2, "Trader_B", "BTCUSDT", "BUY", 65000, 20)  # 🚨 Suspicious
    fraud_system.log_trade(3, "Trader_A", "BTCUSDT", "SELL", 65200, 1.5)
    fraud_system.log_trade(4, "Trader_C", "ETHUSDT", "BUY", 4000, 25)  # 🚨 Suspicious

    suspicious_trades = fraud_system.detect_fraud()
    
    print("\n🚨 Detected Fraudulent Trades:")
    for trade in suspicious_trades:
        print(trade)

    fraud_system.close()

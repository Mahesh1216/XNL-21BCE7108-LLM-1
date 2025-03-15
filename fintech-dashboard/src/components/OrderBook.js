import { useEffect, useState, useRef } from "react";

function OrderBook({ symbol }) {
  const [bids, setBids] = useState([]);
  const [asks, setAsks] = useState([]);
  const wsRef = useRef(null); // Store WebSocket reference

  useEffect(() => {
    const wsUrl = `wss://stream.binance.com:9443/ws/${symbol.toLowerCase()}usdt@depth`;
    
    if (wsRef.current) {
      wsRef.current.close(); // Close existing WebSocket before reconnecting
    }

    wsRef.current = new WebSocket(wsUrl);

    wsRef.current.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);

        if (data?.bids && Array.isArray(data.bids)) {
          setBids(data.bids.slice(0, 5));
        } else {
          console.warn("Invalid bids data:", data.bids);
          setBids([]);
        }

        if (data?.asks && Array.isArray(data.asks)) {
          setAsks(data.asks.slice(0, 5));
        } else {
          console.warn("Invalid asks data:", data.asks);
          setAsks([]);
        }
      } catch (error) {
        console.error("Error parsing WebSocket message:", error);
      }
    };

    wsRef.current.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [symbol]);

  return (
    <div className="bg-gray-900 p-4 rounded-lg text-white">
      <h2 className="text-xl text-center">Order Book ({symbol}/USDT)</h2>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <h3 className="text-red-500">Asks</h3>
          {asks.length > 0 ? (
            asks.map(([price, qty], index) => (
              <p key={index}>{price} ({qty})</p>
            ))
          ) : (
            <p className="text-gray-400">No ask data available</p>
          )}
        </div>
        <div>
          <h3 className="text-green-500">Bids</h3>
          {bids.length > 0 ? (
            bids.map(([price, qty], index) => (
              <p key={index}>{price} ({qty})</p>
            ))
          ) : (
            <p className="text-gray-400">No bid data available</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default OrderBook;

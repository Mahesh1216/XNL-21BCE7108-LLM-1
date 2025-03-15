import { useState } from "react";
import crypto from "crypto";

const API_SECRET = "test_api_secret"; // Replace with your actual secret from backend

export default function TradePanel({ symbol }) {
  const [orderType, setOrderType] = useState("market");
  const [amount, setAmount] = useState(0);
  const [price, setPrice] = useState(0);
  const [side, setSide] = useState("buy");

  const generateSignature = (data) => {
    const payload = `${data.symbol}${data.orderType}${data.amount}${data.price}${data.side}${data.timestamp}`;
    return crypto.createHmac("sha256", API_SECRET).update(payload).digest("hex");
  };

  const handleTradeExecution = async () => {
    const timestamp = Date.now();
    const orderData = {
      symbol,
      orderType,
      amount,
      price: orderType === "market" ? null : price,
      side,
      timestamp,
    };

    // Generate HMAC signature
    orderData.signature = generateSignature(orderData);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/trade/execute", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(orderData),
      });

      const data = await response.json();
      alert(`Order executed: ${JSON.stringify(data)}`);
    } catch (error) {
      alert("Error executing trade");
      console.error("Trade execution error:", error);
    }
  };

  return (
    <div className="bg-gray-800 p-6 rounded-lg text-white w-96 shadow-lg">
      <h2 className="text-xl font-bold text-center">Trade {symbol}/USDT</h2>

      <div className="mt-4">
        <label className="block text-sm">Order Type</label>
        <select
          className="w-full p-2 bg-gray-700 rounded-md"
          value={orderType}
          onChange={(e) => setOrderType(e.target.value)}
        >
          <option value="market">Market</option>
          <option value="limit">Limit</option>
        </select>
      </div>

      {orderType === "limit" && (
        <div className="mt-4">
          <label className="block text-sm">Price</label>
          <input
            type="number"
            className="w-full p-2 bg-gray-700 rounded-md"
            value={price}
            onChange={(e) => setPrice(parseFloat(e.target.value))}
          />
        </div>
      )}

      <div className="mt-4">
        <label className="block text-sm">Amount</label>
        <input
          type="number"
          className="w-full p-2 bg-gray-700 rounded-md"
          value={amount}
          onChange={(e) => setAmount(parseFloat(e.target.value))}
        />
      </div>

      <div className="flex justify-between mt-4">
        <button
          className="bg-green-500 px-4 py-2 rounded-md hover:bg-green-600 w-1/2 mr-2"
          onClick={() => {
            setSide("buy");
            handleTradeExecution();
          }}
        >
          Buy
        </button>
        <button
          className="bg-red-500 px-4 py-2 rounded-md hover:bg-red-600 w-1/2 ml-2"
          onClick={() => {
            setSide("sell");
            handleTradeExecution();
          }}
        >
          Sell
        </button>
      </div>
    </div>
  );
}

import { useEffect, useState, useCallback } from "react";
import OrderBook from "../components/OrderBook";
import TradePanel from "../components/TradePanel"; // ✅ Import TradePanel

export default function Home() {
  const [symbol, setSymbol] = useState("AAPL");
  const [marketType, setMarketType] = useState("stock"); // "stock" or "crypto"
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchMarketData = useCallback(async () => {
    if (!symbol) return;

    setLoading(true);
    setError(null);

    const url =
      marketType === "stock"
        ? `/api/stocks?symbol=${symbol}`
        : `/api/crypto?symbol=${symbol}`;

    try {
      const response = await fetch(url);
      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Failed to fetch market data");
      }

      setData(result);
    } catch (err) {
      setError(err.message);
      setData(null);
    } finally {
      setLoading(false);
    }
  }, [symbol, marketType]);

  useEffect(() => {
    fetchMarketData();

    const interval = setInterval(fetchMarketData, 15000);
    return () => clearInterval(interval);
  }, [fetchMarketData]);

  return (
    <div className="p-10 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold text-center">📊 Market Dashboard</h1>

      {/* 🔹 Search Bar for Stocks & Crypto */}
      <div className="flex justify-center mt-6">
        <input
          type="text"
          placeholder="Enter Symbol (e.g., AAPL, TSLA, BTC)"
          className="p-3 rounded-md bg-white text-black w-64 border border-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value.toUpperCase())}
        />
        <select
          className="ml-2 p-3 bg-gray-800 text-white rounded-md"
          value={marketType}
          onChange={(e) => setMarketType(e.target.value)}
        >
          <option value="stock">Stock</option>
          <option value="crypto">Crypto</option>
        </select>
        <button
          onClick={fetchMarketData}
          className="ml-2 bg-blue-500 px-5 py-3 rounded-md hover:bg-blue-600 transition"
        >
          Search
        </button>
      </div>

      {/* 🔹 Market Data Display */}
      <div className="flex justify-center mt-10">
        <div className="bg-gray-800 p-6 rounded-lg text-center w-96 shadow-lg">
          <h2 className="text-xl font-bold">{symbol} {marketType === "crypto" ? "Crypto" : "Stock"} Price</h2>
          {loading ? (
            <div className="text-lg mt-4 animate-pulse">🔄 Fetching Data...</div>
          ) : error ? (
            <p className="text-red-500 mt-4">{error}</p>
          ) : data ? (
            <>
              <p className="text-4xl font-bold mt-4">${data?.price || "N/A"}</p>
              {marketType === "stock" && (
                <>
                  <p className="text-sm mt-2 text-gray-400">Last Updated: {data?.lastUpdated || "N/A"}</p>
                  <p
                    className={`text-lg font-bold mt-3 ${
                      data?.change?.startsWith("-") ? "text-red-500" : "text-green-500"
                    }`}
                  >
                    {data?.change || "N/A"} ({data?.changePercent || "N/A"})
                  </p>
                </>
              )}
            </>
          ) : (
            <p className="text-gray-400 mt-4">No data available</p>
          )}
        </div>
      </div>

      {/* 🔹 Live Order Book (Crypto Only) */}
      {marketType === "crypto" && (
        <div className="flex justify-center mt-10">
          <OrderBook symbol={symbol} />
        </div>
      )}

      {/* 🔹 Trade Execution Panel (Crypto Only) */}
      {marketType === "crypto" && (
        <div className="flex justify-center mt-10">
          <TradePanel symbol={symbol} /> {/* ✅ Integrate TradePanel */}
        </div>
      )}

      {/* 🔹 Auto-Refresh Indicator */}
      <p className="text-center text-gray-400 mt-6 text-sm">
        Auto-refreshing every 15 seconds...
      </p>
    </div>
  );
}

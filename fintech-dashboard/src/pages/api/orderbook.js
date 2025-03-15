export default async function handler(req, res) {
    if (!req.query.symbol) {
      return res.status(400).json({ error: "Crypto symbol is required" });
    }
  
    const symbol = req.query.symbol.toUpperCase() + "USDT"; // Binance API format
    const url = `https://api.binance.com/api/v3/depth?symbol=${symbol}&limit=5`; // Fetch top 5 bids/asks
  
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error("Failed to fetch data from Binance");
  
      const data = await response.json();
      return res.status(200).json(data);
    } catch (error) {
      return res.status(500).json({ error: error.message });
    }
  }
  
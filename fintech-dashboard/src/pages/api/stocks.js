import axios from "axios";

export default async function handler(req, res) {
  try {
    const { symbol } = req.query;
    const API_KEY = process.env.TWELVE_DATA_API_KEY; // Load API Key

    if (!symbol) {
      return res.status(400).json({ error: "Stock symbol is required" });
    }

    // Fetch stock price from Twelve Data API
    const response = await axios.get(
      `https://api.twelvedata.com/price?symbol=AAPL&apikey=95292b8020114d21978f13fb27aba723`
    );

    if (!response.data.price) {
      return res.status(404).json({ error: `Stock "${symbol}" not found` });
    }

    res.status(200).json({
      symbol: symbol.toUpperCase(),
      price: response.data.price,
    });
  } catch (error) {
    console.error("Stock API Error:", error.message);
    res.status(500).json({ error: "Failed to fetch stock price" });
  }
}

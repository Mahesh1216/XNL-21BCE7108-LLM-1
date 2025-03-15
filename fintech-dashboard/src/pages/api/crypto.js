import axios from "axios";

export default async function handler(req, res) {
  try {
    const { symbol } = req.query;
    const response = await axios.get(
      `https://api.binance.com/api/v3/ticker/price?symbol=${symbol}`
    );

    res.status(200).json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch crypto price" });
  }
}

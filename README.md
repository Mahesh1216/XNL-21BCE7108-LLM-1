# XNL-21BCE7108-LLM-1
🚀 Welcome to the AI-Powered FinTech LLM Trading System!
This project is an end-to-end, high-frequency trading system integrating AI,real-time market monitoring ,focusing on financial data processing, fraud detection, and trading strategy optimization.

Tech Stack :  
✅ Backend: Python, FastAPI, WebSockets, Binance API, Neo4j, PostgreSQL  
✅ Frontend: Next.js, Tailwind CSS  
✅ AI/ML: Hugging Face, OpenAI GPT, XGBoost, LSTMs  
✅ Security & Compliance: OAuth2, JWT, Blockchain-based Audit Logs


✅ Phase 1: FinTech LLM Architecture & Data Ingestion    
Live Market Data & Financial News Scraping
Implemented real-time data ingestion pipelines for:
Stock/crypto/forex data (Binance API, Yahoo Finance)  
Financial news scraping (Bloomberg, Reuters)
Market trend prediction using NLP
Multi-Agent Financial Decision System (partially implemented - 4 agents )  
Developed:
Market Data Aggregator → Scrapes & structures financial news data
LLM Market Sentiment Analyzer → Uses Hugging Face/OpenAI API for news sentiment
Risk Assessment Agent, Trade Execution AI, Fraud Detection Agent Advanced Fraud Detection System (Partially Implemented)
Graph-Based Anomaly Detection using Neo4j (Setup in progress, connection issue pending fix)


✅ Phase 2: AI-Powered Trading Engine & Strategy Testing AI Trading System with Sentiment & Technical Analysis  
Implemented Trading Bot with:
Technical Indicators: RSI, MACD, Bollinger Bands
AI Sentiment Analysis: Hugging Face NLP for news-driven trading
Real-Time Execution: Binance API for automated order placement


completed Backtesting & Strategy Optimization
Implemented:
Vectorized backtesting with historical data
Performance tracking using Sharpe Ratio, Drawdown metrics
A/B Testing for ML models (LSTM & ARAMAI)

Multi-Asset Trading Support (Implemented for Crypto - BTC/USDT)

✅ Phase 3: Full-Stack FinTech UI & Monitoring Dashboard (Partially Implemented) ( its in master branch )

Frontend Development (Next.js + Tailwind CSS)
Developed: Live stock/crypto charts & market data tracking
 Trade Execution Panel & Order Book  
Database & Logging Setup (Partially Implemented)

Database for trade history (PostgreSQL) successfully initialized
Logging & Error Monitoring setup in progress


Prerequisites : 
python = 3.13  
FastAPI: pip install fastapi  
Binance API SDK: pip install python-binance  
Database (PostgreSQL, Redis, Neo4j): pip install psycopg2 redis neo4j  
AI/ML (Hugging Face & OpenAI): pip install openai transformers  
Financial Data (Yahoo Finance, Pandas, NumPy): pip install yfinance pandas numpy  
Visualization & Logging: pip install matplotlib seaborn loguru  

API KEYS :  
Yahoo Finance API   
Binance API     
Hugging Face API

For UI please go to the master branch 

Explanation of phases:
Phase -1 : implemented LLM-powered sentiment analysis to predict market trends using news and social media data. Real-time market data ingestion was set up using Yahoo Finance, Binance API, and Alpha Vantage to fetch stock/crypto updates. A multi-agent financial decision system was built with AI agents for risk assessment, trade execution, and fraud detection. Neo4j-based graph anomaly detection was introduced to detect suspicious trading activities. This phase ensures data-driven trading decisions and regulatory compliance.

Phase-2 : 

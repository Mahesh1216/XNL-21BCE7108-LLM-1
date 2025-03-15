# 📌 Installation & Setup

Follow these steps to set up the **AI-Powered FinTech LLM Trading System** on your local machine.

---

## 1️⃣ **Backend Setup**

```bash
# Clone the repository
git clone https://github.com/Mahesh1216/XNL-21BCE7108-LLM-1/fintech-dashboard.git
cd fintech-dashboard/backend

# Create a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scriptsctivate`

# Install Dependencies
pip install -r requirements.txt

# Start API Server
uvicorn main:app --reload
```

---

## 2️⃣ **Frontend Setup**

```bash
cd fintech-trading-system/frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at **http://localhost:3000**.

---

## 3️⃣ **Database Setup**

Ensure PostgreSQL is installed and running. Then, create the database:

```bash
psql -U postgres -c "CREATE DATABASE fintech_db;"
```

---

## 🚀 **Getting Started with Next.js**

This is a **Next.js project** bootstrapped with `create-next-app`.

### **Run the Development Server**

You can start the server using:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Then, open **[http://localhost:3000](http://localhost:3000)** in your browser to view the app.

---

## 🛠 **Project Structure & API Routes**

- You can start editing the frontend by modifying **pages/index.js**.
- API routes can be accessed at **[http://localhost:3000/api/hello](http://localhost:3000/api/hello)**.
- API endpoints are defined in the `pages/api` directory.

---



🎯 **You're all set! Now build & scale your AI-powered FinTech trading system! 🚀**


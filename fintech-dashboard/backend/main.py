from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import time
import hmac
import hashlib
import os
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from backend.auth import authenticate_user, create_access_token, get_current_user, Token
from backend.oauth import router as oauth_router

app = FastAPI()
app.include_router(oauth_router, prefix="/oauth")
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Trading API!"}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

# Simulated API Key & Secret (Replace with secure storage)
API_KEY = os.getenv("API_KEY", "test_api_key")
API_SECRET = os.getenv("API_SECRET", "test_api_secret")

# Order Data Model
class TradeRequest(BaseModel):
    symbol: str
    orderType: str  # "market" or "limit"
    amount: float
    price: float | None = None  # Price is required for limit orders
    side: str  # "buy" or "sell"
    timestamp: int
    signature: str

def verify_signature(data):
    # Ensure all values are strings before hashing
    payload = f"{data.symbol}{data.orderType}{data.amount}{data.price}{data.side}{data.timestamp}"
    expected_signature = hmac.new(
        API_SECRET.encode(), payload.encode(), hashlib.sha256
    ).hexdigest()

    return expected_signature == data.signature

@app.post("/api/trade/execute")
async def execute_trade(trade: TradeRequest):
    # Verify API Key
    if not verify_signature(trade):
        raise HTTPException(status_code=403, detail="Invalid API signature")

    # Simulate Order Execution (Replace with real trading API)
    order_id = f"ORDER_{int(time.time())}"  # Generate order ID
    execution_price = trade.price if trade.orderType == "limit" else round(50000 + (1000 * (0.5 - time.time() % 1)), 2)  # Fake price simulation

    return {
        "status": "success",
        "orderId": order_id,
        "symbol": trade.symbol,
        "orderType": trade.orderType,
        "side": trade.side,
        "amount": trade.amount,
        "executedPrice": execution_price,
        "timestamp": trade.timestamp,
    }

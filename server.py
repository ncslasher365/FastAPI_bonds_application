from fastapi import FastAPI

app = FastAPI(
    title="Trading application"
)

fake_users_db = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Johh"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

fake_trades_db = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 5.25},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 179, "amount": 8.66},
]


@app.get("/users/{user_id}", tags=["users"])
async def parse_user_information(user_id: int):
    return [user for user in fake_users_db if user.get("id") == user_id]

@app.post("/users/{user_id}", tags=["users"])
def update_user_name(user_id: int, new_name: str):
    try:
        current_user = list(filter(lambda user: user.get("id") == user_id, fake_users_db))[0]
    except IndexError:
        return {"status": 404, "data": "User data not found"}
    if current_user:
        current_user["name"] = new_name
    return {"status": 201, "data": current_user}


@app.get("/trades", tags=["trades"])
async def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades_db[offset : offset + limit]


@app.get("/trades/{trade_id}", tags=["trades"])
async def get_trade_by_id(trade_id: int):
    return [trade for trade in fake_trades_db if trade.get("id") == trade_id]
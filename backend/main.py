from fastapi import FastAPI
from models import User, CheckIn
from storage import DB

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: User):
    return DB.create_user(user)

@app.get("/users")
def list_users():
    return DB.list_users()

@app.post("/users/{user_id}/checkins")
def create_checkin(user_id: str, checkin: CheckIn):
    return DB.create_checkin(user_id, checkin)

@app.get("/users/{user_id}/checkins")
def list_user_checkins(user_id: str):
    return DB.list_checkins(user_id)

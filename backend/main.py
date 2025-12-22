from fastapi import FastAPI, HTTPException

from models import (
    UserCreate, UserOut,
    CheckInCreate, CheckInOut,
    ContactCreate, ContactOut
)
from storage import DB

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# ---------- Users ----------

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    return DB.create_user(user)


@app.get("/users", response_model=list[UserOut])
def list_users():
    return DB.list_users()


# ---------- Contacts ----------

@app.post("/users/{user_id}/contacts", response_model=ContactOut)
def add_contact(user_id: str, contact: ContactCreate):
    try:
        return DB.add_contact(user_id, contact)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/{user_id}/contacts", response_model=list[ContactOut])
def list_contacts(user_id: str):
    try:
        return DB.list_contacts(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")


# ---------- Check-ins ----------

@app.post("/users/{user_id}/checkins", response_model=CheckInOut)
def create_checkin(user_id: str, checkin: CheckInCreate):
    try:
        return DB.create_checkin(user_id, checkin)
    except KeyError as e:
        msg = str(e)
        if "Contact" in msg:
            raise HTTPException(status_code=404, detail=msg)
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/{user_id}/checkins", response_model=list[CheckInOut])
def list_user_checkins(user_id: str):
    try:
        return DB.list_checkins(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")
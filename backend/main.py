from fastapi import FastAPI, HTTPException

# Pydantic models (tu API)
from models import (
    UserCreate,
    UserOut,
    ContactCreate,
    ContactOut,
    CheckInCreate,
    CheckInOut,
)

# In-memory storage (por ahora para contacts/checkins)
from storage import DB

# SQLite / SQLAlchemy (para Users)
from db import Base, engine, SessionLocal
from models_db import UserDB


# Create tables (SQLite)
Base.metadata.create_all(bind=engine)

app = FastAPI()


# ---------- Health ----------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------- Users (SQLite) ----------
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        user_db = UserDB.create(
            name=user.name,
            email=user.email,
        )
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
        return user_db
    finally:
        db.close()


@app.get("/users", response_model=list[UserOut])
def list_users():
    db = SessionLocal()
    try:
        return db.query(UserDB).all()
    finally:
        db.close()


# ---------- Contacts (in-memory) ----------
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


# ---------- Check-ins (in-memory) ----------
@app.post("/users/{user_id}/checkins", response_model=CheckInOut)
def create_checkin(user_id: str, checkin: CheckInCreate):
    try:
        return DB.create_checkin(user_id, checkin)
    except KeyError as e:
        msg = str(e)

        # Si el error habla de un contacto específico, devolvemos ese mensaje
        # (ej: "Contact <id> not found")
        if "Contact" in msg:
            raise HTTPException(status_code=404, detail=msg)

        # Si no, lo tratamos como user not found
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/{user_id}/checkins", response_model=list[CheckInOut])
def list_user_checkins(user_id: str):
    try:
        return DB.list_checkins(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")
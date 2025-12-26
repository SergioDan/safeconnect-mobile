from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import (
    UserCreate, UserOut,
    ContactCreate, ContactOut,
    CheckInCreate, CheckInOut
)

from storage import DB  # lo seguimos usando para contacts/checkins por ahora

from db import Base, engine, SessionLocal
from models_db import UserDB

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# ---- helper: DB session ----
def get_db() -> Session:
    db = SessionLocal()
    try:
        return db
    finally:
        # OJO: esto NO se usa así en FastAPI con Depends;
        # aquí lo dejamos simple porque estamos en modo tutorial.
        pass


# ------------- Users (SQLite) -------------

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        user_db = UserDB.create(name=user.name, email=user.email)
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


# ------------- Contacts (todavía en memoria) -------------

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


# ------------- Check-ins (todavía en memoria) -------------

@app.post("/users/{user_id}/checkins", response_model=CheckInOut)
def create_checkin(user_id: str, checkin: CheckInCreate):
    try:
        return DB.create_checkin(user_id, checkin)
    except KeyError as e:
        msg = str(e)
        raise HTTPException(status_code=404, detail=msg)


@app.get("/users/{user_id}/checkins", response_model=list[CheckInOut])
def list_user_checkins(user_id: str):
    try:
        return DB.list_checkins(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found")
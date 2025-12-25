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

# ---------- Contacts ----------

from db import SessionLocal
from models_db import UserDB, ContactDB


@app.post("/users/{user_id}/contacts", response_model=ContactOut)
def add_contact(user_id: str, contact: ContactCreate):
    db = SessionLocal()
    try:
        # 1) validar que el user exista
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # 2) crear contacto en SQLite
        contact_db = ContactDB.create(
            user_id=user_id,
            name=contact.name,
            phone=contact.phone,
            priority=contact.priority
        )

        db.add(contact_db)
        db.commit()
        db.refresh(contact_db)

        # 3) devolver en formato Pydantic
        return ContactOut(
            id=contact_db.id,
            name=contact_db.name,
            phone=contact_db.phone,
            priority=contact_db.priority
        )
    finally:
        db.close()


@app.get("/users/{user_id}/contacts", response_model=list[ContactOut])
def list_contacts(user_id: str):
    db = SessionLocal()
    try:
        # validar user
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        contacts = (
            db.query(ContactDB)
            .filter(ContactDB.user_id == user_id)
            .order_by(ContactDB.priority.asc())
            .all()
        )

        return [
            ContactOut(
                id=c.id,
                name=c.name,
                phone=c.phone,
                priority=c.priority
            )
            for c in contacts
        ]
    finally:
        db.close()


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
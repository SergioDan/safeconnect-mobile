# backend/main.py
from fastapi import FastAPI, HTTPException

from db import Base, engine, SessionLocal
from models import (
    UserCreate, UserOut,
    ContactCreate, ContactOut,
    CheckInCreate, CheckInOut
)
from models_db import UserDB, ContactDB, CheckInDB

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------------------------
# Helpers: convertir DB -> Pydantic
# -------------------------
def to_user_out(u: UserDB) -> UserOut:
    return UserOut(id=u.id, name=u.name, email=u.email)


def to_contact_out(c: ContactDB) -> ContactOut:
    return ContactOut(id=c.id, name=c.name, phone=c.phone, priority=c.priority)


def to_checkin_out(ch: CheckInDB) -> CheckInOut:
    return CheckInOut(
        id=ch.id,
        user_id=ch.user_id,
        timestamp=ch.timestamp.isoformat(),
        type=ch.type,
        selected_contact_ids=ch.selected_list(),
        notified_contact_ids=ch.notified_list(),
    )


# -------------------------
# Health
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Users (SQLite)
# -------------------------
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        user_db = UserDB.create(name=user.name, email=user.email or "")
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
        return to_user_out(user_db)
    finally:
        db.close()


@app.get("/users", response_model=list[UserOut])
def list_users():
    db = SessionLocal()
    try:
        users = db.query(UserDB).all()
        return [to_user_out(u) for u in users]
    finally:
        db.close()


# -------------------------
# Contacts (SQLite)
# -------------------------
@app.post("/users/{user_id}/contacts", response_model=ContactOut)
def add_contact(user_id: str, contact: ContactCreate):
    db = SessionLocal()
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        contact_db = ContactDB.create(
            user_id=user_id,
            name=contact.name,
            phone=contact.phone,
            priority=contact.priority
        )
        db.add(contact_db)
        db.commit()
        db.refresh(contact_db)
        return to_contact_out(contact_db)
    finally:
        db.close()


@app.get("/users/{user_id}/contacts", response_model=list[ContactOut])
def list_contacts(user_id: str):
    db = SessionLocal()
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        contacts = db.query(ContactDB).filter(ContactDB.user_id == user_id).all()
        return [to_contact_out(c) for c in contacts]
    finally:
        db.close()


# -------------------------
# Check-ins (SQLite)
# -------------------------
@app.post("/users/{user_id}/checkins", response_model=CheckInOut)
def create_checkin(user_id: str, checkin: CheckInCreate):
    db = SessionLocal()
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # (Opcional) Validar que selected_contact_ids existan
        if checkin.selected_contact_ids:
            existing = db.query(ContactDB.id).filter(
                ContactDB.user_id == user_id,
                ContactDB.id.in_(checkin.selected_contact_ids)
            ).all()
            existing_ids = {row[0] for row in existing}
            missing = [cid for cid in checkin.selected_contact_ids if cid not in existing_ids]
            if missing:
                raise HTTPException(status_code=404, detail=f"Contact not found: {missing}")

        checkin_db = CheckInDB.create(
            user_id=user_id,
            type=checkin.type,
            selected_contact_ids=checkin.selected_contact_ids
        )
        db.add(checkin_db)
        db.commit()
        db.refresh(checkin_db)
        return to_checkin_out(checkin_db)
    finally:
        db.close()


@app.get("/users/{user_id}/checkins", response_model=list[CheckInOut])
def list_user_checkins(user_id: str):
    db = SessionLocal()
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        checkins = (
            db.query(CheckInDB)
            .filter(CheckInDB.user_id == user_id)
            .order_by(CheckInDB.timestamp.desc())
            .all()
        )
        return [to_checkin_out(ch) for ch in checkins]
    finally:
        db.close()
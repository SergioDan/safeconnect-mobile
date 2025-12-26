# backend/storage.py
from sqlalchemy.orm import Session
from models_db import UserDB, ContactDB, CheckInDB


class Storage:
    def __init__(self, db: Session):
        self.db = db

    # -------- Users --------
    def create_user(self, user):
        # user: UserCreate (pydantic)
        user_db = UserDB.create(name=user.name, email=user.email or "")
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def list_users(self):
        return self.db.query(UserDB).all()

    def get_user(self, user_id: str):
        user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if not user:
            raise KeyError("User not found")
        return user

    # -------- Contacts --------
    def add_contact(self, user_id: str, contact):
        # contact: ContactCreate (pydantic)
        self.get_user(user_id)  # valida que existe en SQLite

        contact_db = ContactDB.create(
            user_id=user_id,
            name=contact.name,
            phone=contact.phone,
            priority=contact.priority
        )
        self.db.add(contact_db)
        self.db.commit()
        self.db.refresh(contact_db)
        return contact_db

    def list_contacts(self, user_id: str):
        self.get_user(user_id)
        return self.db.query(ContactDB).filter(ContactDB.user_id == user_id).all()

    # -------- Checkins --------
    def create_checkin(self, user_id: str, checkin):
        # checkin: CheckInCreate (pydantic)
        self.get_user(user_id)

        # opcional: validar que los contact_ids existen
        if checkin.selected_contact_ids:
            existing = self.db.query(ContactDB.id).filter(
                ContactDB.user_id == user_id,
                ContactDB.id.in_(checkin.selected_contact_ids)
            ).all()
            existing_ids = {row[0] for row in existing}
            missing = [cid for cid in checkin.selected_contact_ids if cid not in existing_ids]
            if missing:
                raise KeyError(f"Contact not found: {missing}")

        checkin_db = CheckInDB.create(
            user_id=user_id,
            type=checkin.type,
            selected_contact_ids=checkin.selected_contact_ids
        )
        self.db.add(checkin_db)
        self.db.commit()
        self.db.refresh(checkin_db)
        return checkin_db

    def list_checkins(self, user_id: str):
        self.get_user(user_id)
        return self.db.query(CheckInDB).filter(CheckInDB.user_id == user_id).order_by(CheckInDB.timestamp.desc()).all()
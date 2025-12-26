# backend/models_db.py
import uuid
import json
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    contacts = relationship("ContactDB", back_populates="user", cascade="all, delete-orphan")
    checkins = relationship("CheckInDB", back_populates="user", cascade="all, delete-orphan")

    @staticmethod
    def create(name: str, email: str):
        return UserDB(
            id=str(uuid.uuid4()),
            name=name,
            email=email
        )


class ContactDB(Base):
    __tablename__ = "contacts"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)

    user = relationship("UserDB", back_populates="contacts")

    @staticmethod
    def create(user_id: str, name: str, phone: str, priority: int):
        return ContactDB(
            id=str(uuid.uuid4()),
            user_id=user_id,
            name=name,
            phone=phone,
            priority=priority
        )


class CheckInDB(Base):
    __tablename__ = "checkins"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)

    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    type = Column(String, nullable=False)

    # Guardamos listas como JSON en texto para hacerlo simple
    selected_contact_ids = Column(Text, nullable=True)
    notified_contact_ids = Column(Text, nullable=True)

    user = relationship("UserDB", back_populates="checkins")

    @staticmethod
    def create(user_id: str, type: str, selected_contact_ids):
        return CheckInDB(
            id=str(uuid.uuid4()),
            user_id=user_id,
            type=type,
            selected_contact_ids=json.dumps(selected_contact_ids) if selected_contact_ids else None,
            notified_contact_ids=None
        )

    def selected_list(self):
        return json.loads(self.selected_contact_ids) if self.selected_contact_ids else None

    def notified_list(self):
        return json.loads(self.notified_contact_ids) if self.notified_contact_ids else None
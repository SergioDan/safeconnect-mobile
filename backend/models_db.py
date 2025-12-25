import uuid
import json
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from db import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @staticmethod
    def create(name: str, email: str):
        return UserDB(
            id=str(uuid.uuid4()),
            name=name,
            email=email
        )


class CheckInDB(Base):
    __tablename__ = "checkins"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)

    # Ej: "safe" o "need_to_talk" (o lo que uses)
    type = Column(String, nullable=False)

    # Fecha/hora real en DB
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Guardamos listas como JSON en texto para hacerlo simple
    selected_contact_ids = Column(Text, nullable=True)
    notified_contact_ids = Column(Text, nullable=True)

    @staticmethod
    def create(
        user_id: str,
        type: str,
        selected_contact_ids: list[str] | None = None,
        notified_contact_ids: list[str] | None = None,
    ):
        return CheckInDB(
            id=str(uuid.uuid4()),
            user_id=user_id,
            type=type,
            timestamp=datetime.utcnow(),
            selected_contact_ids=json.dumps(selected_contact_ids or []),
            notified_contact_ids=json.dumps(notified_contact_ids or []),
        )
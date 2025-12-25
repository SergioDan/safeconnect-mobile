from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base
import uuid


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


class ContactDB(Base):
    __tablename__ = "contacts"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)

    @staticmethod
    def create(user_id: str, name: str, phone: str, priority: int):
        return ContactDB(
            id=str(uuid.uuid4()),
            user_id=user_id,
            name=name,
            phone=phone,
            priority=priority
        )
import uuid
from sqlalchemy import Column, String
from db import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    @staticmethod
    def create(name: str, email: str | None):
        return UserDB(
            id=str(uuid.uuid4()),
            name=name,
            email=email
        )
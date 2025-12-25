from sqlalchemy import Column, String
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
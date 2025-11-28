from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class CheckInType(str, Enum):
    OK = "OK"
    NEED_TO_TALK = "NEED_TO_TALK"


class UserBase(BaseModel):
    name: str = Field(..., example="Caro")
    email: Optional[str] = Field(None, example="caro@example.com")


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: str


class ContactBase(BaseModel):
    name: str = Field(..., example="Sergio")
    relationship: Optional[str] = Field(None, example="Partner")
    email: Optional[str] = Field(None, example="sergio@example.com")
    phone: Optional[str] = Field(None, example="+57 300 000 0000")
    notify_ok: bool = True
    notify_need_to_talk: bool = True
    is_primary: bool = False


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: str
    user_id: str


class CheckInBase(BaseModel):
    type: CheckInType
    # Lista opcional de contactos a notificar para ESTE check-in
    selected_contact_ids: Optional[List[str]] = None


class CheckInCreate(CheckInBase):
    pass


class CheckIn(CheckInBase):
    id: str
    user_id: str
    timestamp: datetime
    notified_contact_ids: List[str] = []

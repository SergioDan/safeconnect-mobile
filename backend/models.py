from pydantic import BaseModel
from typing import List, Optional

# -------- Requests --------

class UserCreate(BaseModel):
    name: str
    email: Optional[str] = None


class ContactCreate(BaseModel):
    name: str
    phone: str
    priority: int


class CheckInCreate(BaseModel):
    type: str  # "OK" | "NEED_TO_TALK"
    selected_contact_ids: Optional[List[str]] = None


# -------- Responses --------

class UserOut(BaseModel):
    id: str
    name: str
    email: Optional[str] = None


class ContactOut(BaseModel):
    id: str
    name: str
    phone: str
    priority: int


class CheckInOut(BaseModel):
    id: str
    user_id: str
    timestamp: str
    type: str
    selected_contact_ids: Optional[List[str]] = None
    notified_contact_ids: Optional[List[str]] = None
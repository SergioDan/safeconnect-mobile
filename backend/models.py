from pydantic import BaseModel
from typing import List, Optional


# ---------- Requests ----------

class UserCreate(BaseModel):
    name: str
    email: Optional[str] = None


class CheckInCreate(BaseModel):
    type: str  # "OK" or "NEED_TO_TALK"
    selected_contact_ids: Optional[List[str]] = None


class ContactCreate(BaseModel):
    name: str
    phone: str
    priority: int


# ---------- Responses / Stored Models ----------

class UserOut(BaseModel):
    id: str
    name: str
    email: Optional[str] = None


class CheckInOut(BaseModel):
    id: str
    user_id: str
    timestamp: str
    type: str
    selected_contact_ids: Optional[List[str]] = None
    notified_contact_ids: Optional[List[str]] = None


class ContactOut(ContactCreate):
    id: str
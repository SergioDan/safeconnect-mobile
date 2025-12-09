from pydantic import BaseModel
from typing import List, Optional
import datetime

class User(BaseModel):
    id: str
    name: str
    email: Optional[str] = None

class CheckIn(BaseModel):
    user_id: str
    type: str  # "OK" o "NEED_TO_TALK"
    timestamp: str = datetime.datetime.utcnow().isoformat()
    selected_contact_ids: Optional[List[str]] = None

import uuid
from datetime import datetime
from typing import Dict, List

from .models import User, UserCreate, Contact, ContactCreate, CheckIn, CheckInCreate


class InMemoryStorage:
    """
    Simple in-memory storage for demo purposes.
    This can be replaced later by a real database (e.g. PostgreSQL + SQLAlchemy).
    """

    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
        self.contacts: Dict[str, Contact] = {}
        self.checkins: Dict[str, CheckIn] = {}

    # Users

    def create_user(self, payload: UserCreate) -> User:
        user_id = str(uuid.uuid4())
        user = User(id=user_id, **payload.dict())
        self.users[user_id] = user
        return user

    def get_user(self, user_id: str) -> User | None:
        return self.users.get(user_id)

    def list_users(self) -> List[User]:
        return list(self.users.values())

    # Contacts

    def create_contact(self, user_id: str, payload: ContactCreate) -> Contact:
        contact_id = str(uuid.uuid4())
        contact = Contact(id=contact_id, user_id=user_id, **payload.dict())
        self.contacts[contact_id] = contact
        return contact

    def list_contacts_for_user(self, user_id: str) -> List[Contact]:
        return [c for c in self.contacts.values() if c.user_id == user_id]

    # Check-ins

    def create_checkin(self, user_id: str, payload: CheckInCreate) -> CheckIn:
        checkin_id = str(uuid.uuid4())
        checkin = CheckIn(
            id=checkin_id,
            user_id=user_id,
            timestamp=datetime.utcnow(),
            type=payload.type,
            selected_contact_ids=payload.selected_contact_ids,
            notified_contact_ids=payload.selected_contact_ids or [],
        )
        self.checkins[checkin_id] = checkin
        return checkin

    def list_checkins_for_user(self, user_id: str) -> List[CheckIn]:
        return [c for c in self.checkins.values() if c.user_id == user_id]


# instancia global para el demo
storage = InMemoryStorage()

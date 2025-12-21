from uuid import uuid4
from datetime import datetime
from typing import Dict, List
from models import ContactCreate, ContactOut

from models import UserCreate, UserOut, CheckInCreate, CheckInOut


class Storage:
    def __init__(self):
        self.users: Dict[str, UserOut] = {}
        self.checkins: Dict[str, List[CheckInOut]] = {}

self.contacts: Dict[str, List[ContactOut]] = {}

    def create_user(self, user: UserCreate) -> UserOut:
        user_id = str(uuid4())
        stored = UserOut(
            id=user_id,
            name=user.name,
            email=user.email
        )
        self.users[user_id] = stored
        return stored

    def list_users(self) -> List[UserOut]:
        return list(self.users.values())

    def create_checkin(self, user_id: str, checkin: CheckInCreate) -> CheckInOut:
        if user_id not in self.users:
            raise KeyError("User not found")
# Validate selected contacts
if checkin.selected_contact_ids:
    contacts = self.contacts.get(user_id, [])
    contact_ids = {c.id for c in contacts}

    for cid in checkin.selected_contact_ids:
        if cid not in contact_ids:
            raise KeyError(f"Contact {cid} not found")
        checkin_id = str(uuid4())
        stored = CheckInOut(
            id=checkin_id,
            user_id=user_id,
            timestamp=datetime.utcnow().isoformat(),
            type=checkin.type,
            selected_contact_ids=checkin.selected_contact_ids,
            notified_contact_ids=None
        )

        if user_id not in self.checkins:
            self.checkins[user_id] = []
        self.checkins[user_id].append(stored)

        return stored

    def list_checkins(self, user_id: str) -> List[CheckInOut]:
        return self.checkins.get(user_id, [])


DB = Storage()
def add_contact(self, user_id: str, contact: ContactCreate) -> ContactOut:
    if user_id not in self.users:
        raise KeyError("User not found")

    contact_id = str(uuid4())
    stored = ContactOut(
        id=contact_id,
        name=contact.name,
        phone=contact.phone,
        priority=contact.priority
    )

    if user_id not in self.contacts:
        self.contacts[user_id] = []

    self.contacts[user_id].append(stored)
    return stored


def list_contacts(self, user_id: str) -> List[ContactOut]:
    if user_id not in self.users:
        raise KeyError("User not found")

    return self.contacts.get(user_id, [])
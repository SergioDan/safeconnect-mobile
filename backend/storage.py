from models import User, CheckIn

class Storage:
    def __init__(self):
        self.users = {}
        self.checkins = {}

    def create_user(self, user: User):
        self.users[user.id] = user
        return user

    def list_users(self):
        return list(self.users.values())

    def create_checkin(self, user_id: str, checkin: CheckIn):
        if user_id not in self.checkins:
            self.checkins[user_id] = []
        self.checkins[user_id].append(checkin)
        return checkin

    def list_checkins(self, user_id: str):
        return self.checkins.get(user_id, [])

DB = Storage()

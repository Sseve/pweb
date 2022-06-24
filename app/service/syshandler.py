import json


class UserHandler:
    def __init__(self, db):
        self.db = db

    async def check_user(self, user):
        val = {"name": json.loads(user)["username"]}
        sql = "SELECT * FROM user WHERE name = :name"
        if await self.db.fetch_all(query=sql, values=val):
            return True
        return False
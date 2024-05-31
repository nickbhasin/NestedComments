from quart import g

from utils import UserName, UserPost


async def register_user_dao(data: UserName):
    result = await g.connection.fetch_one(
        """INSERT INTO user (name) VALUES (:name) RETURNING id, name""", {"name": data.name},
    )
    return result


async def get_users_dao():
    query = """SELECT * FROM user"""
    result = [UserPost(**row) async for row in g.connection.iterate(query)]
    return result
from quart import g
from datetime import datetime
from utils import PostDataUser, UserID, Posts


async def add_posts_dao(data: PostDataUser):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO post (title, created_at, user_id) VALUES (:title, :created_at, :user_id) RETURNING user_id, 
        title, post_id""", {"title": data.title, "created_at": datetime.now(), "user_id": data.user_id},
    )
    if result:
        like_dislike = await g.connection.fetch_one("""INSERT INTO post_likes_dislikes (post_id, 
        knowledge_begin_date, likes, dislikes) VALUES (:post_id, :knowledge_begin_date, :likes, :dislikes)""",
                                                    {"post_id": result['post_id'], "knowledge_begin_date":
                                                        datetime.now(), "likes": 0, "dislikes": 0})
    return result


async def get_all_posts_by_user_dao(data: UserID):
    query = """SELECT post_id, title, created_at FROM post WHERE user_id = {}""".format(data.user_id)
    result = [Posts(**row) async for row in g.connection.iterate(query)]
    return result

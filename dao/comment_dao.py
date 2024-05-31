from quart import g
from datetime import datetime

from utils import CommentPost, FetchComments, Comments, CommentID


async def add_comment_dao(data: CommentPost):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO comment (title, created_at, user_id, parent_comment_id, post_id, is_parent) VALUES (:title, :created_at, 
        :user_id, :parent_comment_id, :post_id, :is_parent) RETURNING title, comment_id""", {"title": data.title, "created_at":
            datetime.now(), "user_id": data.user_id, "post_id":data.post_id, "parent_comment_id":data.parent_comment_id, "is_parent": data.is_parent},
    )
    if data.parent_comment_id:
        result1 = await g.connection.fetch_one("""UPDATE comment SET is_parent = {} WHERE comment_id = {} RETURNING
        comment_id""".format("true", data.parent_comment_id),)
    if result:
        like_dislike = await g.connection.fetch_one("""INSERT INTO comment_likes_dislikes (comment_id, 
        knowledge_begin_date, likes, dislikes) VALUES (:comment_id, :knowledge_begin_date, :likes, :dislikes)""",
                                                    {"comment_id": result['comment_id'], "knowledge_begin_date":
                                                        datetime.now(), "likes": 0, "dislikes": 0})
    return result


async def get_all_comments_on_post_dao(data: FetchComments):
    query = """SELECT user_id, title, created_at FROM comment WHERE post_id = {} and parent_comment_id = {} ORDER BY 
    created_at""".format(data.post_id, data.parent_comment_id) if data.parent_comment_id else """SELECT user_id, 
    title, created_at FROM comment WHERE post_id = {} and parent_comment_id is null ORDER BY created_at""".format(
        data.post_id)
    result = [Comments(**row) async for row in g.connection.iterate(query)]
    return result


async def get_all_replies_on_comment_dao(data: CommentID):
    query = ("""SELECT user_id, title, created_at FROM comment WHERE parent_comment_id = {} ORDER BY created_at""".
             format(data.comment_id))
    result = [Comments(**row) async for row in g.connection.iterate(query)]
    return result

from quart import g
from datetime import datetime

from utils import PostLike, CommentLike, PostID, CommentID


async def add_dislikes_to_post_dao(data: PostLike):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO post_dislikes (user_id, post_id, knowledge_begin_date, knowledge_end_date) VALUES (:user_id, 
        :post_id, :knowledge_begin_date, null) RETURNING id""", {"knowledge_begin_date": datetime.now(), "user_id":
            data.user_id, "post_id":data.post_id},)
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result1 = await g.connection.fetch_one(
        """UPDATE post_likes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and post_id = {} 
        RETURNING id""".format(string, data.user_id, data.post_id),)
    if result:
        return "Disliked!!!"
    return None


async def add_dislikes_to_comment_dao(data: CommentLike):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO comment_dislikes (user_id, comment_id, knowledge_begin_date, knowledge_end_date) VALUES (
        :user_id, :comment_id, :knowledge_begin_date, null) RETURNING id""", {"knowledge_begin_date": datetime.now(),
                                                                              "user_id": data.user_id,
                                                                              "comment_id":data.comment_id},)
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result1 = await g.connection.fetch_one(
        """UPDATE comment_likes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and comment_id = {} 
        RETURNING id""".format(string, data.user_id, data.comment_id),)
    if result:
        return "Disliked!!!"
    return None


async def remove_dislikes_to_post_dao(data: PostLike):
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result = await g.connection.fetch_one(
        """UPDATE post_dislikes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and post_id = {} 
        RETURNING id""".format(string, data.user_id, data.post_id),)
    if result:
        return "Dislike Removed!!!"
    return None


async def remove_dislikes_to_comment_dao(data: CommentLike):
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result = await g.connection.fetch_one(
        """UPDATE comment_dislikes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and comment_id = 
        {} RETURNING id""".format(string, data.user_id, data.comment_id),)
    if result:
        return "Dislike Removed!!!"
    return None


async def view_dislikes_to_post_dao(data: PostID):
    query = """SELECT DISTINCT user_id FROM post_dislikes WHERE post_id = {} and knowledge_end_date is null ORDER 
            BY knowledge_begin_date""".format(data.post_id)
    result = [row['user_id'] async for row in g.connection.iterate(query)]
    if result:
        query2 = """SELECT name FROM user WHERE id in ({});""".format(",".join(str(element) for element in result))
        result2 = [row['name'] async for row in g.connection.iterate(query2)]
        if result2:
            return result2
    return []


async def view_dislikes_to_comment_dao(data: CommentID):
    query = """SELECT DISTINCT user_id FROM comment_dislikes WHERE comment_id = {} and knowledge_end_date is null 
            ORDER BY knowledge_begin_date""".format(data.comment_id)
    result = [row['user_id'] async for row in g.connection.iterate(query)]
    if result:
        query2 = """SELECT name FROM user WHERE id in ({});""".format(",".join(str(element) for element in result))
        result2 = [row['name'] async for row in g.connection.iterate(query2)]
        if result2:
            return result2
    return []


async def view_total_dislikes_to_post_dao(data: PostID):
    query = """SELECT dislikes as total_dislikes FROM post_likes_dislikes WHERE post_id = {}""".format(data.post_id)
    result = await g.connection.fetch_one(query)
    return str(result["total_dislikes"])


async def view_total_dislikes_to_comment_dao(data: CommentID):
    query = """SELECT dislikes as total_dislikes FROM comment_likes_dislikes WHERE comment_id = {}""".format(data.comment_id)
    result = await g.connection.fetch_one(query)
    return str(result["total_dislikes"])

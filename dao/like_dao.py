from quart import g
from datetime import datetime

from utils import PostLike, CommentLike, PostID, CommentID


async def add_likes_to_post_dao(data: PostLike):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO post_likes (user_id, post_id, knowledge_begin_date, knowledge_end_date) VALUES (:user_id, 
        :post_id, :knowledge_begin_date, null) RETURNING id""", {"knowledge_begin_date": datetime.now(), "user_id":
            data.user_id, "post_id":data.post_id},
    )
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result1 = await g.connection.fetch_one(
        """UPDATE post_dislikes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and post_id = {} 
        RETURNING id""".format(
            string, data.user_id, data.post_id),
    )
    if result:
        return "Liked!!!"
    return None


async def add_likes_to_comment_dao(data: CommentLike):
    r = await g.connection.fetch_one("""PRAGMA foreign_keys = ON;""")
    result = await g.connection.fetch_one(
        """INSERT INTO comment_likes (user_id, comment_id, knowledge_begin_date, knowledge_end_date) VALUES (
        :user_id, :comment_id, :knowledge_begin_date, null) RETURNING id""", {"knowledge_begin_date": datetime.now(),
                                                                              "user_id": data.user_id,
                                                                              "comment_id":data.comment_id},
    )
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result1 = await g.connection.fetch_one(
        """UPDATE comment_dislikes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and comment_id = {} 
        RETURNING id""".format(
            string, data.user_id, data.comment_id),
    )
    if result:
        return "Liked!!!"
    return None


async def remove_likes_to_post_dao(data: PostLike):
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result = await g.connection.fetch_one(
        """UPDATE post_likes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and post_id = {} 
        RETURNING id""".format(string, data.user_id, data.post_id),
    )
    if result:
        return "Like Removed!!!"
    return None


async def remove_likes_to_comment_dao(data: CommentLike):
    now = datetime.now()
    string = now.strftime('%Y-%m-%d')
    result = await g.connection.fetch_one(
        """UPDATE comment_likes SET knowledge_end_date = CAST({} AS DATETIME) WHERE user_id = {} and comment_id = {} 
        RETURNING id""".format(string, data.user_id, data.comment_id),
    )
    if result:
        return "Like Removed!!!"
    return None


async def view_likes_to_post_dao(data: PostID):
    query = """SELECT DISTINCT user_id FROM post_likes WHERE post_id = {} and knowledge_end_date is null ORDER BY 
            knowledge_begin_date""".format(data.post_id)
    result = [row['user_id'] async for row in g.connection.iterate(query)]
    if result:
        query2 = """SELECT name FROM user WHERE id in ({});""".format(",".join(str(element) for element in result))
        result2 = [row['name'] async for row in g.connection.iterate(query2)]
        if result2:
            return result2
    return []


async def view_likes_to_comment_dao(data: CommentID):
    query = """SELECT DISTINCT user_id FROM comment_likes WHERE comment_id = {} and knowledge_end_date is null 
            ORDER BY knowledge_begin_date""".format(data.comment_id)
    result = [row['user_id'] async for row in g.connection.iterate(query)]
    if result:
        query2 = """SELECT name FROM user WHERE id in ({});""".format(",".join(str(element) for element in result))
        result2 = [row['name'] async for row in g.connection.iterate(query2)]
        if result2:
            return result2
    return []


async def update_likes_dislikes_post_dao(data: PostID):
    query1 = """SELECT COUNT(DISTINCT user_id) as total_likes FROM post_likes WHERE post_id = {} and 
            knowledge_end_date is null""".format(data.post_id)
    result1 = await g.connection.fetch_one(query1)
    query2 = """SELECT COUNT(DISTINCT user_id) as total_dislikes FROM post_dislikes WHERE post_id = {} and 
            knowledge_end_date is null""".format(data.post_id)
    result2 = await g.connection.fetch_one(query2)
    if result1 and result2:
        result = await g.connection.fetch_one(
            """UPDATE post_likes_dislikes SET likes = {} and dislikes = {} WHERE post_id = {} RETURNING id""".format(str(result1['total_likes']), str(result2['total_dislikes']), data.post_id),
        )
        if result:
            return "Updated!!!"
    return "Not Updated!!!"


async def view_total_likes_to_post_dao(data: PostID):
    query = """SELECT likes as total_likes FROM post_likes_dislikes WHERE post_id = {}""".format(data.post_id)
    result = await g.connection.fetch_one(query)
    return str(result["total_likes"])


async def update_likes_dislikes_comment_dao(data: CommentID):
    query1 = """SELECT COUNT(DISTINCT user_id) as total_likes FROM comment_likes WHERE comment_id = {} and 
            knowledge_end_date is null""".format(data.comment_id)
    result1 = await g.connection.fetch_one(query1)
    query2 = """SELECT COUNT(DISTINCT user_id) as total_dislikes FROM comment_dislikes WHERE comment_id = {} and 
            knowledge_end_date is null""".format(data.comment_id)
    result2 = await g.connection.fetch_one(query2)
    if result1 and result2:
        result = await g.connection.fetch_one(
            """UPDATE comment_likes_dislikes SET likes = {}, dislikes = {} WHERE comment_id = {} RETURNING id""".
            format(str(result1['total_likes']), str(result2['total_dislikes']), data.comment_id),
        )
        if result:
            return "Updated!!!"
    return "Not Updated!!!"


async def view_total_likes_to_comment_dao(data: CommentID):
    query = """SELECT likes as total_likes FROM comment_likes_dislikes WHERE comment_id = {}""".format(
        data.comment_id)
    result = await g.connection.fetch_one(query)
    return str(result["total_likes"])

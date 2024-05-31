from quart import Blueprint, g, abort
from quart_schema import validate_request

from dao.like_dao import add_likes_to_comment_dao, add_likes_to_post_dao, remove_likes_to_post_dao, \
    remove_likes_to_comment_dao, view_likes_to_post_dao, update_likes_dislikes_post_dao, view_total_likes_to_post_dao, \
    update_likes_dislikes_comment_dao, view_likes_to_comment_dao, view_total_likes_to_comment_dao
from utils import PostLike, CommentLike, CommentID, \
    PostID

like_service_blueprint = Blueprint('like_service_blueprint', __name__)


@like_service_blueprint.post("/addLikesToPost/")
@validate_request(PostLike)
async def add_likes_to_post(data: PostLike):
    """Add Likes to Post"""
    result = await add_likes_to_post_dao(data)
    if result:
        return "Liked!!!"
    return abort(404)


@like_service_blueprint.post("/addLikesToComment/")
@validate_request(CommentLike)
async def add_likes_to_comment(data: CommentLike):
    """Add Likes to Comment"""
    result = await add_likes_to_comment_dao(data)
    if result:
        return "Liked!!!"
    return abort(404)


@like_service_blueprint.delete("/removeLikesToPost/")
@validate_request(PostLike)
async def remove_likes_to_post(data: PostLike):
    """Remove Likes to Post"""
    result = await remove_likes_to_post_dao(data)
    if result:
        return "Like Removed!!!"
    return abort(404)


@like_service_blueprint.delete("/removeLikesToComment/")
@validate_request(CommentLike)
async def remove_likes_to_comment(data: CommentLike):
    """Remove Likes to Comment"""
    result = await remove_likes_to_comment_dao(data)
    if result:
        return "Like Removed!!!"
    return abort(404)


@like_service_blueprint.post("/viewLikeToPost/")
@validate_request(PostID)
async def view_likes_to_post(data: PostID):
    """View Likes to Post"""
    result = await view_likes_to_post_dao(data)
    return result


@like_service_blueprint.post("/viewLikeToComment/")
@validate_request(CommentID)
async def view_likes_to_comment(data: CommentID):
    """View Likes to Comment"""
    result = await view_likes_to_comment_dao(data)
    return result


@like_service_blueprint.put("/updateLikesDislikesToPost/")
@validate_request(PostID)
async def update_likes_dislikes_post(data: PostID):
    """Update Total Likes/Dislikes to Post"""
    result = await update_likes_dislikes_post_dao(data)
    return result


@like_service_blueprint.post("/viewTotalLikeToPost/")
@validate_request(PostID)
async def view_total_likes_to_post(data: PostID):
    """View Total Likes to Post"""
    result = await view_total_likes_to_post_dao(data)
    return result


@like_service_blueprint.put("/updateLikesDislikesToComment/")
@validate_request(CommentID)
async def update_likes_dislikes_comment(data: CommentID):
    """Update Total Likes/Dislikes to Comment"""
    result = await update_likes_dislikes_comment_dao(data)
    return result


@like_service_blueprint.post("/viewTotalLikeToComment/")
@validate_request(CommentID)
async def view_total_likes_to_comment(data: CommentID):
    """View Total Likes to Comment"""
    result = await view_total_likes_to_comment_dao(data)
    return result

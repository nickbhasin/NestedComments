from quart import Blueprint, abort
from quart_schema import validate_request

from dao.dislike_dao import add_dislikes_to_post_dao, add_dislikes_to_comment_dao, remove_dislikes_to_post_dao, \
    remove_dislikes_to_comment_dao, view_dislikes_to_post_dao, view_dislikes_to_comment_dao, \
    view_total_dislikes_to_post_dao, view_total_dislikes_to_comment_dao
from utils import PostLike, CommentLike, CommentID, \
    PostID

dislike_service_blueprint = Blueprint('dislike_service_blueprint', __name__)


@dislike_service_blueprint.post("/addDislikeToPost/")
@validate_request(PostLike)
async def add_dislikes_to_post(data: PostLike):
    """Add Dislikes to Post"""
    result = await add_dislikes_to_post_dao(data)
    if result:
        return result
    return abort(404)


@dislike_service_blueprint.post("/addDislikeToComment/")
@validate_request(CommentLike)
async def add_dislikes_to_comment(data: CommentLike):
    """Add Dislikes to comment"""
    result = await add_dislikes_to_comment_dao(data)
    if result:
        return result
    return abort(404)


@dislike_service_blueprint.delete("/removeDislikesToPost/")
@validate_request(PostLike)
async def remove_dislikes_to_post(data: PostLike):
    """Remove Dislikes to Post"""
    result = await remove_dislikes_to_post_dao(data)
    if result:
        return result
    return abort(404)


@dislike_service_blueprint.delete("/removeDislikesToComment/")
@validate_request(CommentLike)
async def remove_dislikes_to_comment(data: CommentLike):
    """Remove Dislikes to Comment"""
    result = await remove_dislikes_to_comment_dao(data)
    if result:
        return result
    return abort(404)


@dislike_service_blueprint.post("/viewDislikeToPost/")
@validate_request(PostID)
async def view_dislikes_to_post(data: PostID):
    """View DisLikes to Post"""
    result = await view_dislikes_to_post_dao(data)
    return result


@dislike_service_blueprint.post("/viewDislikeToComment/")
@validate_request(CommentID)
async def view_dislikes_to_comment(data: CommentID):
    """View DisLikes to Comment"""
    result = await view_dislikes_to_comment_dao(data)
    return result


@dislike_service_blueprint.post("/viewTotalDislikeToPost/")
@validate_request(PostID)
async def view_total_dislikes_to_post(data: PostID):
    """View Total Dislikes to Post"""
    result = await view_total_dislikes_to_post_dao(data)
    return result


@dislike_service_blueprint.post("/viewTotalDislikeToComment/")
@validate_request(CommentID)
async def view_total_dislikes_to_comment(data: CommentID):
    """View Total Dislikes to Comment"""
    result = await view_total_dislikes_to_comment_dao(data)
    return result

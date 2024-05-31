from quart import Blueprint
from quart_schema import validate_request, validate_response

from dao.comment_dao import add_comment_dao, get_all_comments_on_post_dao, get_all_replies_on_comment_dao
from utils import CommentPost, CommentData, FetchComments, CommentList, CommentID

comment_service_blueprint = Blueprint('comment_service_blueprint', __name__)


@comment_service_blueprint.post("/addComment/")
@validate_request(CommentPost)
@validate_response(CommentData)
async def add_comment(data: CommentPost) -> CommentData:
    """Add Comment"""
    result = await add_comment_dao(data)
    return CommentData(**result)


@comment_service_blueprint.post("/viewComments")
@validate_request(FetchComments)
@validate_response(CommentList)
async def get_all_comments_on_post(data: FetchComments) -> CommentList:
    """Get All Comments on a Post"""
    result = await get_all_comments_on_post_dao(data)
    return CommentList(comments=result)


@comment_service_blueprint.post("/viewReplies")
@validate_request(CommentID)
@validate_response(CommentList)
async def get_all_replies_on_comment(data: CommentID) -> CommentList:
    """Get All Replies on a Comment"""
    result = await get_all_replies_on_comment_dao(data)
    return CommentList(comments=result)

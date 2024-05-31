from quart import Blueprint
from quart_schema import validate_request, validate_response

from dao.post_dao import add_posts_dao, get_all_posts_by_user_dao
from utils import PostDataUser, PostData, PostList, UserID

post_service_blueprint = Blueprint('post_service_blueprint', __name__)


@post_service_blueprint.post("/addPost/")
@validate_request(PostDataUser)
@validate_response(PostData)
async def add_posts(data: PostDataUser) -> PostData:
    """Add Posts"""
    result = await add_posts_dao(data)
    return PostData(**result)


@post_service_blueprint.post("/getAllPost/")
@validate_request(UserID)
async def get_all_posts_by_user(data: UserID) -> PostList:
    """Get All Posts of a User"""
    result = await get_all_posts_by_user_dao(data)
    return PostList(posts=result)

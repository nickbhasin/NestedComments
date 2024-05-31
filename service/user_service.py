from quart import Blueprint
from quart_schema import validate_request, validate_response

from dao.user_dao import register_user_dao, get_users_dao
from utils import UserName, UserPost, Users

user_service_blueprint = Blueprint('user_service_blueprint', __name__)


@user_service_blueprint.post("/userRegistration/")
@validate_request(UserName)
@validate_response(UserPost)
async def register_user(data: UserName) -> UserPost:
    """Register User"""
    result = await register_user_dao(data)
    return UserPost(**result)


@user_service_blueprint.get("/getAllUsers/")
@validate_response(Users)
async def get_users() -> Users:
    """Get All Users"""
    result = await get_users_dao()
    return Users(users=result)


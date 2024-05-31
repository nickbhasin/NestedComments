import sqlite3

from quart import Quart
from quart_db import QuartDB
from quart_schema import QuartSchema

from service.comment_service import comment_service_blueprint
from service.dislike_service import dislike_service_blueprint
from service.like_service import like_service_blueprint
from service.post_service import post_service_blueprint
from service.user_service import user_service_blueprint
from table_creation import creation

app = Quart(__name__)
connection = sqlite3.connect("database.db")
QuartDB(app, url="sqlite:///database.db")
QuartSchema(app)

creation()
app.register_blueprint(user_service_blueprint, url_prefix="/social_network")
app.register_blueprint(post_service_blueprint, url_prefix="/social_network")
app.register_blueprint(comment_service_blueprint, url_prefix="/social_network")
app.register_blueprint(like_service_blueprint, url_prefix="/social_network")
app.register_blueprint(dislike_service_blueprint, url_prefix="/social_network")






from flask import Blueprint
from flask_restful import Api
from webapp.users.controller.controller import TemplateController, UserSignUpController,\
    \
    UserLoginController, RetrieveInfo

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_blueprint)

user_api.add_resource(TemplateController, "/template")
user_api.add_resource(UserSignUpController, "/signup")
user_api.add_resource(UserLoginController, "/login")
user_api.add_resource(RetrieveInfo, "/info")

posts_blueprint = Blueprint('post', __name__, url_prefix='/api/post')
posts_api = Api(posts_blueprint)


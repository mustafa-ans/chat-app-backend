from flask.views import MethodView
from flask import request
from webapp.users.service.service import UserService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

global token


class UserLoginController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        input_data = request.get_json()
        email = input_data['email']
        password = input_data['password']
        user_id = self.service.check_login(email, password)

        if user_id is None:
            return {
                       "data": {},
                       "status": "fail",
                       "message": "incorrect username or password"
                   }, 401

        access_token = create_access_token(identity=user_id)
        return {
            "data": {
                "token": access_token
            },
            "status": "success",
            "message": "Successfully logged in"
        }


class TemplateController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        input_data = request.get_json()
        user_id = input_data['user_id']

        user_info = self.service.template(user_id)

        return {
            "data": user_info,
            "status": "success",
            "message": ""
        }


class UserSignUpController(MethodView):
    def __init__(self):
        self.service = UserService()

    def post(self):
        input_data = request.get_json()
        first_name = input_data['first_name']
        last_name = input_data['last_name']
        email = input_data['email']
        username = input_data['username']
        password = input_data['password']
        confirm_password = input_data['confirm_password']
        # TODO create a service layer method that takes in the above inputs and creates an account on the database

        self.service.signup(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            username=username,
                            password=password,
                            confirm_password=confirm_password)

        error = self.service.signup(first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    username=username,
                                    password=password,
                                    confirm_password=confirm_password)

        if error is not None:
            return {
                "data": {},
                "status": "fail",
                "message": error
            }
        else:
            return {
                "data": {},
                "status": "success",
                "message": "New user was successfully created"
            }


class RetrieveInfo(MethodView):

    def __init__(self):
        self.service = UserService()

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user_info = self.service.retrieve_info(user_id)
        return {
            "data": user_info
        }

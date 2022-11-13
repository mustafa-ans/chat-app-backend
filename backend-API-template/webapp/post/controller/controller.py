from flask.views import MethodView
from flask import request
from webapp.post.service.service import PostService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


class SharePostController(MethodView):
    def __init__(self):
        self.service = PostService()

    @jwt_required()  # This declares that this method can only be called with a JWT token
    def post(self):
        input_data = request.get_json()
        message = input_data['message']  # Post message is stored in the "message" field
        user_id = get_jwt_identity()  # JWT token contains the user id as identity.
        post_id = self.service.share_post(user_id, message)  # Service logic not implemented yet, but we know what
        # values we pass in, and what values to get back

        return {
            "data": {
                "post_id": post_id
            },
            "error": None,
            "status": "success"
        }

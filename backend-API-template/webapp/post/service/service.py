from webapp.post.dao.dao import PostDAO


class PostService:
    def __init__(self):
        self.dao = PostDAO()

    def share_post(self, user_id: str, message: str):
        post_id = self.dao.share_post(user_id, message)

        return post_id

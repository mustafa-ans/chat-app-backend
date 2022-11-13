from common_lib.infra.mysql import DB
from uuid import uuid4


class PostDAO:
    def __init__(self):
        self.db = DB()

    def share_post(self, user_id, message):
        # Copy the query from Workbench and replace the values with %()s string replacers
        query = """
        INSERT INTO post
        (id, user_id, message)
        VALUES
        (%(post_id)s, %(user_id)s, %(message)s);
        """
        # Create a new uuid4 post_id
        post_id = str(uuid4())
        # Declare Query Params
        params = {
            "post_id": post_id,
            "user_id": user_id,
            "message": message
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)

            return post_id

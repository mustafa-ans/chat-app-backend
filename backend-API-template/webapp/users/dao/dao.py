from common_lib.infra.mysql import DB
from uuid import uuid4


class UserDAO:
    def __init__(self):
        self.db = DB()

    def template(self, user_id):
        query = """
                SELECT id 
                , first_name
                , last_name
                , prof_pic_url
                , email
                FROM user
                WHERE USER_ID = %(user_id)s
                """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "user_id": user_id
            })
            row = cursor.fetchone()

            user = {
                "user_id": row['id'],
                "email": row['EMAIL'],
                "first_name": row['FIRST_NAME'],
                "last_name": row['LAST_NAME'],
                "prof_pic_url": row['PROF_PIC_URL']
            }

            return user

    def check_email(self, email: str):
        query = """
                SELECT id from user
                WHERE email = %(email_query)s
                """

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "email_query": email
            })
            row = cursor.fetchone()

            if row is not None:
                return True
            else:
                return False

    def check_username(self, username: str):
        query = """
                SELECT username from user
                WHERE username = %(username_query)s
                """
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "username_query": username
            })
            row = cursor.fetchone()

            if row is not None:
                return True
            else:
                return False

    def signup(self, first_name: str, last_name: str, email: str, username: str, password: str):
        query = """"
        INSERT INTO user
        (id, first_name, last_name, email, username, password)
        VALUES
        (%(id)s, %(first_name)s, %(last_name)s, %(email)s, %(username)s, %(password)s;
        """
        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, {
                "id": str(uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "username": username,
                "password": password
            })

    def check_login(self, email, password):
        query = f"""
        SELECT id from user
        WHERE email = %(email)s
        AND password = %(password)s;
        """

        params = {
            "email": email,
            "password": password
        }

        with self.db.cursor(dictionary=True) as cursor:
            cursor.execute(query, params)
            row = cursor.fetchone()

            if row is None:
                return None
            else:
                return row['id']

    def retrieve_info(self, user_id):
        with self.db.cursor(dictionary=True) as cursor:
            query = """
                            SELECT id,
                            first_name
                            , last_name
                            , prof_pic_url
                            , email
                            FROM user
                            WHERE id = %(user_id)s
                            """

            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute(query, {
                    "user_id": user_id
                })
                row = cursor.fetchone()

                user = {
                    "user_id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "prof_pic_url": row['prof_pic_url'],
                    "email": row['email']
                }

                return user

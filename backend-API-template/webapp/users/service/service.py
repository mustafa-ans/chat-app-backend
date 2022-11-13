from webapp.users.dao.dao import UserDAO


class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def template(self, user_id: str):
        return self.dao.template(user_id)

    def signup(self,
               first_name: str,
               last_name: str,
               email: str,
               username: str,
               password: str,
               confirm_password: str):
        if confirm_password != password:
            return "Passwords do not match"

        email_exists = self.dao.check_email(email)
        if email_exists:
            return "An account with the same email address exists"
        username_exists = self.dao.check_username(username)
        if username_exists:
            return "Username already exists"
        self.dao.signup(first_name, last_name, email, username, password)

    def check_login(self, email, password):
        user_id = self.dao.check_login(email, password)

        return user_id

    def retrieve_info(self, user_id):

        return self.dao.retrieve_info(user_id)

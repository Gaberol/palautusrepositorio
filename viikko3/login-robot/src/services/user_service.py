from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username is too short")

        if len(password) < 8:
            raise UserInputError("Password is too short")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username can only include letters a-z")
        

        #Regex ei toiminu :(((
#        if not re.match("[^a-z]", password):
#            raise UserInputError("Password can not contain only letters a-z")

        password_check = False
        for c in password:
            if c not in ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                         "j", "k", "l", "m", "n", "o", "p", "q", "r",
                         "s", "t", "u", "v", "w", "x", "y", "z"
                         ]:
                password_check = True
        if not password_check:
            raise UserInputError("Password can not contain only letters a-z")

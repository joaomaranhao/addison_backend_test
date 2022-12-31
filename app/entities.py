class Credentials:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password


class User:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id


class UserToken:
    def __init__(self, token: str) -> None:
        self.token = token

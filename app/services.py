from interfaces import SyncTokenServiceInterface
from entities import Credentials, User, UserToken


class SyncTokenService(SyncTokenServiceInterface):
    def _authenticate(self, credentials: Credentials) -> User:
        return User(credentials.username)

    def _issue_token(self, user: User) -> UserToken:
        return UserToken("any_token")

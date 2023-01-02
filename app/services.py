import asyncio
from interfaces import SyncTokenServiceInterface, AsyncTokenServiceInterface
from entities import Credentials, User, UserToken


class SyncTokenService(SyncTokenServiceInterface):
    def _authenticate(self, credentials: Credentials) -> User:
        return User(credentials.username)

    def _issue_token(self, user: User) -> UserToken:
        return UserToken("any_token")


class AsyncTokenService(AsyncTokenServiceInterface):
    async def _authenticate(self, credentials: Credentials) -> User:
        return User(credentials.username)

    async def _issue_token(self, user: User) -> UserToken:
        return UserToken("any_token_ASYNC")

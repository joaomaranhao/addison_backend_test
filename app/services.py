import random
import asyncio
from datetime import datetime
from .interfaces import SyncTokenServiceInterface, AsyncTokenServiceInterface
from .entities import Credentials, User, UserToken


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


class SimpleAsyncTokenService(AsyncTokenService):
    async def _authenticate(self, credentials: Credentials) -> User:
        await asyncio.sleep(random.randint(0, 5))
        if credentials.password == credentials.username.upper():
            user = User(credentials.username)
            return user
        else:
            raise Exception("Invalid username or password!")

    async def _issue_token(self, user: User) -> UserToken:
        await asyncio.sleep(random.randint(0, 5))
        if user.user_id[0] == "A":
            raise Exception("User ID cannot starts with 'A'")
        formatted_token = user.user_id + "_" + str(datetime.now().isoformat())
        user_token = UserToken(formatted_token)
        return user_token

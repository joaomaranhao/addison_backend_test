from abc import ABC, abstractmethod
from entities import Credentials, User, UserToken


class SyncTokenServiceInterface(ABC):
    @abstractmethod
    def _authenticate(self, credentials: Credentials) -> User:
        pass

    @abstractmethod
    def _issue_token(self, user: User) -> UserToken:
        pass

    def request_token(self, credentials: Credentials) -> UserToken:
        authenticated_user = self._authenticate(credentials)
        if not authenticated_user:
            raise Exception("Invalid username or password")
        return self._issue_token(authenticated_user)


class AsyncTokenServiceInterface:
    @abstractmethod
    async def _authenticate(self, credentials: Credentials) -> User:
        pass

    @abstractmethod
    async def _issue_token(self, user: User) -> UserToken:
        pass

    async def request_token(self, credentials: Credentials) -> UserToken:
        authenticated_user = await self._authenticate(credentials)
        if not authenticated_user:
            raise Exception("Invalid username or password")
        user_token = await self._issue_token(authenticated_user)
        return user_token

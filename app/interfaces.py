from abc import ABC, abstractmethod
from typing import Awaitable
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
    def _authenticate(self, credentials: Credentials) -> Awaitable[User]:
        raise NotImplementedError

    def _issue_token(self, user: User) -> Awaitable[UserToken]:
        raise NotImplementedError

    def request_token(self, credentials: Credentials) -> Awaitable[UserToken]:
        raise NotImplementedError

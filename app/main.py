from services import SyncTokenService, AsyncTokenService, SimpleAsyncTokenService
from entities import Credentials
import asyncio


async def main():
    c = Credentials("any_username", "any_password")
    valid_credentials = Credentials("house", "HOUSE")
    # Sync Service
    service = SyncTokenService()
    token = service.request_token(c)
    print(token.token)

    # Async Service
    service2 = AsyncTokenService()
    token2 = await service2.request_token(c)
    print(token2.token)

    # Simple Async Token Service
    service3 = SimpleAsyncTokenService()
    token3 = await service3.request_token(valid_credentials)
    print(token3.token)


if __name__ == "__main__":
    asyncio.run(main())

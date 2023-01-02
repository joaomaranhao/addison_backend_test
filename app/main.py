from services import SyncTokenService, AsyncTokenService
from entities import Credentials
import asyncio


async def main():
    c = Credentials("any_username", "any_password")
    # Sync Service
    service = SyncTokenService()
    token = service.request_token(c)
    print(token.token)

    # Async Service
    service2 = AsyncTokenService()
    token2 = await service2.request_token(c)
    print(token2.token)


if __name__ == "__main__":
    asyncio.run(main())

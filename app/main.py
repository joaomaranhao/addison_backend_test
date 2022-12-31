from services import SyncTokenService
from entities import Credentials


def main():
    c = Credentials("any_username", "any_password")
    service = SyncTokenService()
    token = service.request_token(c)
    print(token.token)


if __name__ == "__main__":
    main()

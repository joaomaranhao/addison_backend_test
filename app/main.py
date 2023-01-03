from .services import SimpleAsyncTokenService
from .entities import Credentials
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


class CredentialsModel(BaseModel):
    username: str
    password: str


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")


@app.post("/login")
async def login(credentials: CredentialsModel):
    try:
        c = Credentials(credentials.username, credentials.password)
        service = SimpleAsyncTokenService()
        token = await service.request_token(c)
        return token.token
    except Exception as err:
        return {"error": err.args[0]}

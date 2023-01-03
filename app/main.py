from .services import SimpleAsyncTokenService
from .entities import Credentials
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")


@app.post("/login")
async def login(username: str, password: str):
    try:
        c = Credentials(username, password)
        service = SimpleAsyncTokenService()
        token = await service.request_token(c)
        return token.token
    except Exception as err:
        return {"error": err.args[0]}

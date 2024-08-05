from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


@app.get("/yc")
async def login():
    return {"沒ㄐㄐ"}

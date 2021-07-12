from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

class RegIn(BaseModel):
    username: str
    password: str
    email: str

class RegOut(BaseModel):
    username: str
    email: str

@app.post("/register", response_model=RegOut)
async def register(user: RegIn):
    #user.password = hashlib.sha1(user.password.encode('utf-8')).hexdigest()
    return user
from pydantic import BaseModel
from fastapi import FastAPI
import hashlib
app = FastAPI()

class UserInput(BaseModel):
    name: str
    username: str
    password: str

class UserOutput(BaseModel):
    name: str
    username: str
    #password: str

@app.post("/user/", response_model= UserOutput)
async def user(user: UserInput):
    # Do whatever, store the pass etc
    #user.password = hashlib.sha1(user.password.encode("utf-8")).hexdigest()
    return user
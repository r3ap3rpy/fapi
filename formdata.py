from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...), email: str = Form(...) ):
    return {'username': username, 'password': password, 'email':email}

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username':username, 'password': password}


#import requests
#s = requests.Session()
#s.post(url="http://127.0.0.1:8000/login/",data={"username":"dszabo","password":"12345"})
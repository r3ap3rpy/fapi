from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def index():
    return {"Hello":'World'}

#uvicorn 1:api --reload
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/redoc
#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/openapi.json
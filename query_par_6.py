from fastapi import FastAPI

api = FastAPI(title = "Query parameters!")

@api.get("/")
async def qpars(a:int,b:int,c:int):
    return {'a':a,'b':b,c:'c'}

#http://localhost:8000/?a=10&b=11&c=12
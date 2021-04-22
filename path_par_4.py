from fastapi import FastAPI

api = FastAPI()


@api.get("/beer/{typeName}")
async def bartender(typeName : str):
    return {"Type of Beer" : typeName}


@api.get("/beer/jollyjoker")
async def bartender():
    return {"Type of Beer" : 'JJ'}


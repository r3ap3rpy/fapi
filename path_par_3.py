from fastapi import FastAPI

api = FastAPI()

@api.get("/beer/{typeName}")
async def bartender(typeName : int):
    return {"Type of Beer" : typeName}
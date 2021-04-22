from fastapi import FastAPI

api = FastAPI()

@api.get("/beer/{typeName}")
async def bartender(typeName):
    return {"Type of Beer" : typeName}
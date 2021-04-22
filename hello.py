from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

class ModellName(str, Enum):
    alexnet = "alexnet"
    lenet  = "lenet"
    restnet = "restnet"


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    fake_db = [_ for _ in range(skip+limit)]
    return fake_db[skip : skip+limit]

@app.get("/models/{model_name}")
async def get_model(model_name: ModellName):
    return {"model_name":model_name}

@app.get("/item/{item_id}")
async def get_item(item_id: int):
    return {"item_id":item_id}

@app.get("/")
async def root():
    return {"message":"hello"}

@app.get("/foods/{food_id}")
async def foodz(food_id: str, q: Optional[str] = None):
    if q:
        return {"q":q, "food_id":food_id }
    else:
        return {"food_id" : food_id}
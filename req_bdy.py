from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Beer(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float

class Vine(BaseModel):
    name: str
    origin: str
    vine_type: str

class Shots(BaseModel):
    name: str

Inventory = {
    "Shots":{"Whiskey":100,"Palinka":50}
}

app = FastAPI()

@app.post("/beers/")
async def create_beer(beer: Beer):
    return beer

@app.post("/vines/{vine_id}")
async def vines(vine_id: int, vine: Vine):
    return {vine_id: vine}

@app.post("/shots/}")
async def shots(shots: Shots, quantity: int):
    print(shots.name)
    if Inventory["Shots"].get(shots.name):
        return {'price': Inventory["Shots"][shots.name] * quantity}
    else:
        return "N.A."


#import requests
#requests.post(url="http://127.0.0.1:8000/beers", data=json.dumps({'name':'Buddweiser','description':'Well this is tecnically not a beer','price':300,'quantity':12})).text
#requests.post(url="http://127.0.0.1:8000/vines/1", data=json.dumps({'name':'Aszu','origin':'Hungary','vine_type':'dry'})).text
#requests.post(url="http://127.0.0.1:8000/shots/%7D?quantity=10", data=json.dumps({'name':'Whiskey'})).text

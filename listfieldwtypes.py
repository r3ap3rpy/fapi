from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Beer(BaseModel):
    name: str
    flavour: str
    tags: List[str] = []

@app.put("/beers/{beer_id}")
async def update_beer(beer_id: int, beer: Beer):
    return {"beer_id":beer_id, "beer" : beer}


#requests.put(url="http://127.0.0.1:8000/beers/10",data=json.dumps({"name":"Kozel","flavour":"sweet","tags":["XI District","Budapest","hungary"]}))

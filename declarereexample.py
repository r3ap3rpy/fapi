from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Beer(BaseModel):
    name: str
    description: str
    class Config:
        schema_extra = {
            "example" : {
                "name" : "Soproni",
                "description" : "A Hungarian beer!"
            }
        }

    
@app.put("/beers/{beer_id}")
async def update_beer(beer_id:int, beer: Beer):
    return {'beer_id':beer_id, "beer":beer}

# See under schemas
from enum import Enum
from fastapi import FastAPI

class Beer(str, Enum):
    Staropramen = "Staropramen"
    Bellevue = 'Bellevue'
    Buddweiser = 'Buddweiser'

api = FastAPI()

@api.get("/beers/{beername}")
async def bartender(beername: Beer):
    if beername == Beer.Staropramen:
        return {"1" : "Good Choice" }
    elif beername == Beer.Bellevue:
        return {"2" : "Even better choice" }
    else:
        return {"3" : "Would you mind reconsidering?" }


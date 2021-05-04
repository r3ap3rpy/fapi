from enum import Enum
from fastapi import FastAPI

class Beer(str, Enum):
    Staropramen = "Staropramen"
    Bellevue = "Bellevue"
    Buddweiser = "Buddweiser"

api = FastAPI()

@api.get("/beer/{typeName}")
def beer(typeName : str):
    if typeName == Beer.Staropramen:
        return {"Choice" : "Good!"}
    elif typeName == Beer.Bellevue:
        return {"Choice" : "Great!"}
    else:
        return {"Choice" : "You can do better!"}

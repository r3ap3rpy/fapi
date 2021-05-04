from fastapi import FastAPI

api = FastAPI()

@api.get("/beer/{typeName}")
def beer(typeName : str):
    return {"Type of beer" : typeName}
    
@api.get("/price/{itemId}")
def price(itemId : float):
    if itemId > 100:
        return {"That will cost you!" : itemId * 1000}
    else:
        return {"Thats not so bad!" : itemId * 10}
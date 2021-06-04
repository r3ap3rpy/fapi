from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/serial/")
async def minmax(q: Optional[str] = Query(None,min_length=7 , max_length=7)):
    if q:
        return {"serial" : q}
    return {"serial" : "Was not specified!"}

@app.get("/rep/")
async def rep(q: Optional[List[str]] = Query(None, min_length=3,max_length=3)):
    if q:
        return {'3q-s':','.join(q)}
    return {'q-s':'Were not specified!'}

@app.get("/deflist/")
async def deflist(q: Optional[List[str]] = Query(["one","two"])):
    return q

@app.get("/desc/")
async def desc(q: Optional[str] = Query(None, title='This is the title!',description="This is the description!")):
    return {"q":"Description and Title example!"}

@app.get("/alias/")
async def aliasing(q: Optional[str] = Query(None)):
    return "Alias example!"

@app.get("/depr/")
async def deprecated(q: Optional[str] = "default",r: Optional[str] = Query("deprecated",deprecated=True)):
    return {'q':q,'r':r}
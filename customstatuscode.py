from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=210)
async def index():
    return {'customstatuscode' : 'get'}

@app.post("/post", status_code=220)
async def posted():
    return {'customstatuscode' : 'post'}

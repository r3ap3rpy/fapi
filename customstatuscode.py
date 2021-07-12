from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=211)
async def index():
    return {"custom":"status_code"}
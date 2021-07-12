from fastapi import FastAPI, Cookie, Header
from typing import Optional
app = FastAPI()

@app.get("/beers")
def beers(beer_cookie: Optional[str] = Cookie(None), beer_header: Optional[str] =   Header(None)):
    return {"beer_coodike": beer_cookie, "beer_header": beer_header}

# see in docs
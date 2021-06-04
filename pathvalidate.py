from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

Beerz = {
    "Kozel" : {'Quality': 'Fine', 'Available' : 10, 'Price' : 200},
    "Soproni" : {'Quality' : "Not bad", 'Available': 20, 'Price' : 100}
}

@app.get("/beer/{beer_name}")
async def beer(beer_name: str = Path('Kozel',title="The name of the beer!"), order: Optional[int] = Query(None, gt=0)):
    if Beerz.get(beer_name):
        if order:
            if Beerz[beer_name]['Available'] >= order:
                return {beer_name : {'Total Price' : (order*Beerz[beer_name]['Price']),'Remaining':(Beerz[beer_name]['Available'] - order)}}

            return {beer_name : {'Status':'Not Enough in stock','Available':Beerz[beer_name]['Available'],'Ordered':order}}
        return {beer_name : Beerz[beer_name]}
    else:
        return {beer_name : "Unavailable"}


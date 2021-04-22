from fastapi import FastAPI
from typing import Optional
from enum import Enum


api = FastAPI()

@api.get("/qpar/{mandatory}")
async def manopt(mandatory : str, notsomandatory: Optional[str] = None):
    item = {'mandatory':mandatory}
    if notsomandatory:
        item.update({'mandatory':mandatory,'notsomandatory':notsomandatory})
    return item


@api.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/qpar/yoloo?notsomandatory=20
#http://127.0.0.1:8000/items/foo?short=true
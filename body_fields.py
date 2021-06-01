from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Computer(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="The owner of machine and it's purpose!",max_length=50)
    serial: str
    model: str
    price: float = Field(...,gt=0, description="The price of the machine!")

@app.put("/inventory/{machine_id}")
async def update(machine_id: int, machine: Computer = Body(...,embed=True)):
    return {"machine_id":machine_id,"machine":machine}

#import requests
#requests.put(url="http://127.0.0.1:8000/inventory/10",data=json.dumps({"machine":{"name":"HUNDB1","description":"Database server for Daniel","serial":"aosdakndsak","model":"HP Probook","price":100}})).text
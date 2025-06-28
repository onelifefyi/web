from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def root():
    return {"Hello": "World!!"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

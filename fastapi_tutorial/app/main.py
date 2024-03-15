from fastapi import FastAPI
from pydantic import BaseModel


# create app instance
app = FastAPI()


# create Item class
class Item(BaseModel):
    id: int
    content: str
    finished: bool = False


# create a heap memory for storing todo
item_arr = []


@app.post("/items")
async def create_item(item: Item):
    # store the item inside array
    item_arr.append(item)
    return {"message": "item created successfully"}


@app.delete("/items/{id}")
async def delete_todo(id: int):
    for i, item in enumerate(item_arr):
        if item.id == id:
            del item_arr[i]
        return {"message": "item has been deleted"}
    return {"message": "item not found!"}


@app.get("/")
async def read_todo():
    return {"id":0, "content":"hello world!" , "finished":True}



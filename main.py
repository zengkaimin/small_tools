from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    name: str

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"test"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/inoreader/starred")
def rsync_inoreader_starred(item:Item):
    return {"test"}

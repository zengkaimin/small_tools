from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str

app = FastAPI()

@app.get("/")
def read_root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"test"}
#test

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    '''_summary_'''
    print("hahha")
    #test
    print (item_id)
    return {"item_id": item_id, "q": q}

@app.post("/inoreader/starred")
def rsync_inoreader_starred(item:Item):


    print('zengkaimin')
    return {"test"}

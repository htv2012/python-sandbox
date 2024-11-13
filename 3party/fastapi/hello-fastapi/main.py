import logging
from typing import Optional

import fastapi

logging.basicConfig(level="INFO")  # There must be a better way

app = fastapi.FastAPI()


@app.get("/")
def get_index():
    return {"message": "Success"}


DB = {
    501: {"alias": "kevin", "shell": "bash"},
    502: {"alias": "anna", "shell": "zsh"},
}


@app.get("/items/")
def get_all():
    return DB


@app.get("/items/{item_id}")
def get_item(item_id: Optional[int] = None):
    print(f"GET item_id={item_id}")
    logging.info("GET item_id=%r", item_id)
    if item_id is None:
        return {"ids": DB.keys()}
    try:
        result = DB[item_id]
        return result
    except KeyError:
        raise fastapi.HTTPException(404)

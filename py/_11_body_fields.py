from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# You can use Pydantic's Field to declare extra validations and metadata for model attributes.
# The same way you can declare additional validation and metadata in path operation function parameters with Query, Path and Body, 
# you can declare validation and metadata inside of Pydantic models using Pydantic's Field.

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title='The description of the item', max_length=300)
    price: float | None = Field(gt=0, descritpion='The price must be greater than 0')
    tax: float | None = None

@app.put('/items{item_id}')
async def read_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {'item_id': item_id, 'item': item}
    return results
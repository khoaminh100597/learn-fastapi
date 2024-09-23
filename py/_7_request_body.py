from fastapi import FastAPI
# Step 1: Import Pydantic's BaseModel
from pydantic import BaseModel
from typing import List
import requests
import pandas as pd

# Request Body
# A request body is data sent by the client to your API. 
# A response body is the data your API sends to the client.

# Step 2: Create your data model
# This is the request body
# The same as when declaring query parameters, when a model attribute has a default value, it is not required. 
# Otherwise, it is required. Use None to make it just optional.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
app = FastAPI()

# Step 3: Declare it as a parameter
@app.post('/items/{item_id}')
async def create_item(item_id: int, item: Item):
    item_dict = item.model_dump() # Convert it to dictionary. Note remember .model_dump() for convert object (BaseModel) to Dict
    # editor support
    item_dict['name'] = item_dict['name'] + '_fixed'
    if item_dict['tax']:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    # df = pd.DataFrame([data.model_dump() for data in item])
    # print(df)
    return {'item_id': item_id, **item_dict}

@app.post('/multiitems/')
async def create_multi_items(items: List[Item]):
    df = pd.DataFrame([item.model_dump() for item in items]) # Convert List[Item] to DataFrame
    print(df)
    lst = []
    for item in items:
        item_dict = item.model_dump() # Convert it to dictionary
        # editor support
        item_dict['name'] = item_dict['name'] + '_fixed'
        if item_dict['tax']:
            price_with_tax = item.price + item.tax
            item_dict.update({'price_with_tax': price_with_tax})
        lst.append(item_dict)
    # return {"message": "Data received successfully", "data": df.to_dict(orient='records')}
    return lst

# Results
# Read the body of the request as JSON.
# Convert the corresponding types (if needed).
# Validate the data.
# If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.
# Give you the received data in the parameter item.
# As you declared it in the function to be of type Item, 
# you will also have all the editor support (completion, etc) for all of the attributes and their types.
# Generate JSON Schema definitions for your model, you can also use them anywhere else you like if it makes sense for your project.

# Remember

# The function parameters will be recognized as follows:

# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
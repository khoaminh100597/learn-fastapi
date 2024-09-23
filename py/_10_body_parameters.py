from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    fullname: str | None = None

# Mix Path, Query and body parameters
@app.post('/items/{item_id}')
async def read_items(item_id: Annotated[int|None, Path(title='The ID of item to get', ge=0, le=1000)],
                     q: str | None = None,
                     item: Item | None = None):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        item = item.model_dump()
        item['price_tax'] = item['price'] + item['tax']
        results.update({'item': item})
    return results
# The request body of above example is
# # {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }


# Multiple body parameters
# @app.put('/users/{item_id}')
# async def read_user(item_id: int, user: User, item: Item):
#     results = {'item_id': item_id}

#     if user:
#         results.update({'user': user})

#     if item:
#         results.update({'item': item})

#     return results
# The request body of above example is
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }


# Singular values in body
# The same way there is a Query and Path to define extra data for query and path parameters, FastAPI provides an equivalent Body.
# @app.put('/users/{item_id}')
# async def read_user(item_id: int, user: User, item: Item, importance: Annotated[bool | None, Body()] = False):
#     results = {'item_id': item_id}

#     if user:
#         results.update({'user': user})

#     if item:
#         results.update({'item': item})

#     if importance:
#         results.update({'importance': importance})

#     return results

# The request body of example is
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance": 5
# }


# Multiple body params and query
# you can also declare additional query parameters whenever you need, additional to any body parameters.
# As, by default, singular values are interpreted as query parameters, you don't have to explicitly add a Query

# Embe a single body parameter
# Let's say you only have a single item body parameter from a Pydantic model Item.
# By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents, 
# as it does when you declare extra body parameters, you can use the special Body parameter embed:
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# The request body of above example is:
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }

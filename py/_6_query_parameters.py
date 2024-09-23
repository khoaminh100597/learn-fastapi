from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Query parameters
# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
# As query parameters are not a fixed part of a path, they can be optional and can have default values.

# @app.get('/items/')
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# In the example above they have default values of skip=0 and limit=10.
# So, going to the URL:
# http://127.0.0.1:8000/items/
# would be the same as going to:
# http://127.0.0.1:8000/items/?skip=0&limit=10

# Optional parameters
# The same way, you can declare optional query parameters, by setting their default to None

# @app.get('/items/{item_id}')
# async def read_item(item_id:str, q: str | None = None):
#     if q:
#         return {'item_id': item_id, 'q': q}
#     return {'item_id': item_id}

# Query parameter type conversion
# You can also declare bool types, and they will be converted
# or http://127.0.0.1:8000/items/foo?short=1
# or http://127.0.0.1:8000/items/foo?short=True
# or http://127.0.0.1:8000/items/foo?short=true
# or http://127.0.0.1:8000/items/foo?short=on
# or http://127.0.0.1:8000/items/foo?short=yes
# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {'item_id': item_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {'description': "This is an amazing item that has a long description"}
#         )
#     return item

# Multiple path and query parameters
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({
            'description': "This is an amazing item that has a long description"
        })

    return item

# Required query parameters
# When you want to make a query parameter required, you can just not declare any default value:
@app.get('/items/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item
# ...without adding the required parameter needy, you will see an error like:
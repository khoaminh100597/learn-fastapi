from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

# Additional validation of string parameters
# we enforce its length does not exceed 50 characters

app = FastAPI()

# Remember using Annotated and Query in path parameters for string validation
# max_length, min_length, pattern (for regex)
# @app.get('/')
# async def read_items(q: Annotated[str | None, Query(max_length=50, min_length=3, pattern="^fixedquery$")] = None):
#     results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
#     return results

# Required with eclips (...)
# you can declare that a parameter can accept None, but that it is still required
# @app.get('/items')
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
#     results = {'item': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
#     return results

# Query parameters list / multiple values
# When you define a query parameter explicitly with Query 
# you can also declare it to receive a list of values, or said in other way, to receive multiple values.
# @app.get('/items')
# async def read_items(q: Annotated[list[int], Query()] = None):
#     query_items = {'q': q}
#     return query_items

# Query parameter list / multiple values with defaults
# And you can also define a default list of values if none are provided:
# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items

# Declare more metadata
# You can add more information about the parameter. Such as a title, a description
# @app.get('/items')
# async def read_items(q: Annotated[str | None, Query(title='Query string',
#                                                     description='Query string for the items to search in the database that have a good match',
#                                                     min_length=3)] = None):
#     results = {'items': [{'item_id': 'Foo',
#                           'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
    
#     return results

# Alias parameters
# You can declare an alias, and that alias is what will be used to find the parameter value:
# @app.get('/items')
# async def read_items(q: Annotated[str | None, Query(alias='query-parameters')] = None):
#     results = {'items': [{'item_id': 'Foo',
#                           'item_id': 'Bar'}]}
#     if q:
#         results.update({'q': q})
    
#     return results

# Deprecating parameters
# Now let's say you don't like this parameter anymore.
# You have to leave it there a while because there are clients using it, but you want the docs to clearly show it as deprecated.
# Then pass the parameter deprecated=True to Query:
@app.get('/items')
async def read_items(q: Annotated[str | None, Query(deprecated=True)] = None):
    results = {'items': [{'item_id': 'Foo',
                          'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    
    return results

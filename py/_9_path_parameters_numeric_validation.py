from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

# In the same way that you can declare more validations and metadata for query parameters with Query, 
# you can declare the same type of validations and metadata for path parameters with Path.

# @app.get('/items')
# async def read_items(q: Annotated[str | None, Query()] = None,
#                      item_id: Annotated[int | None, Path()] = None):
    
#     results = {'item_id': item_id}
#     return results

# Declare metadata
# Add a title, description

# Remember the parameters with no default value should be before the parameters with default values
# @app.get('/items/{item_id}')
# async def read_items(item_id: Annotated[int, Path()],
#                      q: Annotated[str | None, Query()] = None):
    
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results

# We can use * to delcare the parameters in function should be called key-values pairs, 
# it does not matter the parameters with or without default value
# @app.get('/items/{item_id}')
# async def read_items(*,
#                      item_id: int = Path(description='The id of the item'),
#                      q: str,
#                      ):
    
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results

# We should practice using Annotated
# Annotated can combine with Query, Path, sometimes we do not need to declare the default value like above

# Number validation: greater than or equal "gt" "ge"
# @app.get('/items/{item_id}')
# async def read_items(item_id: Annotated[int, Path(description='The ID of item to get', ge=1)],
#                      q: str):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results
## Number validation: less than or equal "lt" "le"
@app.get('/items/{item_id}')
async def read_items(item_id: Annotated[int, Path(description='The ID of item to get', lt=10)],
                     q: str):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

# With Query and Path, you can declare number constraints.
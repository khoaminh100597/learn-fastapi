from fastapi import FastAPI
from enum import Enum


app = FastAPI()

# Path parameters with types
# You can declare the type of a path parameter in the function
# Data conversion, Data validation
@app.get('/{item_id}')
async def root(item_id: int):
    return(f'The result is {item_id}')

# Order matters. When creating path operations, you can find situations where you have a fixed path.
# Like /users/me, let's say that it's to get data about the current user.
# And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.
# Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

# Predefined values¶
# Create an Enum class, that inherits from str and Enum
# By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.


class Model(str, Enum):
    alexnet = 'model_alexnet'
    resnet = 'model_resnet'
    lenet = 'model_lenet'

class Id(int, Enum):
    alexnet = 1
    resnet = 2
    lenet = 3

@app.get('/model/{model_name}')
async def get_model(model_name: Model):
    # The value of the path parameter will be an enumeration member. 
    # You can compare it with the enumeration member in your created enum ModelName
    if model_name is Model.alexnet:
        id = Id.alexnet
        return {"model_name": model_name, "message": "Deep Learning FTW!", "id": id.value}
    elif model_name.value == 'model_lenet': # Get the enumeration value
        id = Id.lenet
        return {"model_name": model_name, "message": "LeCNN all the images", "id": id.value}
    else:
        id = Id.resnet
        return {"model_name": model_name, "message": "Have some residuals", "id": id.value}
    
# Path convertor
# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:
# /files/{file_path:path}
# In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("_5_path_parameters:app", host='0.0.0.0', port=8000, log_level='info', reload=True)
# Step 1: import FastAPI
from fastapi import FastAPI

# Step 2: create a FastAPI "instance"
app = FastAPI()

# Step 3: create a path operation
# Operation could be POST, GET, PUT, DELETE
# Define a path operation decorator
@app.get('/')
# Step 4: define the path operation function
async def root():
# Step 5: return the content
    return {'message': 'Hello World'}
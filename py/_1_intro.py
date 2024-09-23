from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    
    name: str ='Lan'
    price: float = 9999
    is_offer: Union[bool, None] = None


@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/items/{item_id}/{item_name}')
def read_item(item_id:int, item_name: str):
    item = Item(name=item_name)
    return {'name': item.name, 
            'price': item.price,}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item': item.name, 'item_id': item_id}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', log_level='info')
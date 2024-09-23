from _7_request_body import Item
import requests
import pandas as pd

# Remember, when post a request body, we should convert it to dictitonary by model.dump()
# Remember, when returning, we should return a dictionary or a List[Item]

# Example 1: 
# item = Item(name='minhnhk', description='long_description', price=1000, tax=123)

# response = requests.post('http://127.0.0.1:8000/items/5',
#                          json=item.model_dump())

# print(response.json())
# print(type(response.json()))

# Example 2:

df = pd.DataFrame({
    'name': ['minhnhk', 'nhid'],
    'description': ['long', 'short'],
    'price': [1000, 1200],
    'tax': [110, 114]
})

df_json = df.to_dict(orient='records')

## List[Item]
print(df_json)
print(type(df_json))

response = requests.post('http://127.0.0.1:8000/multiitems',
                         json=df_json)

df = pd.DataFrame(response.json())
print(df)
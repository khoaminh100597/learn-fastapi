import requests
import pandas as pd
from _10_body_parameters import Item

# Mix Path, Query and body parameters

# Method 1: From dataframe -> To list of dict -> dict
# df = pd.DataFrame({
#     'name': ['Car'],
#     'description': ['Honda'],
#     'price': [1000],
#     'tax': [100]
# })

# df_dict = df.to_dict(orient='records')[0]

# Method 2: Dict
# data_dict = {
#     'name': 'Car',
#     'description': 'Honda',
#     'price': 1000,
#     'tax': 100
# }

# item_id = 10
# q = 'special'

# response = requests.post(f'http://127.0.0.1:8000/items/{item_id}?q={q}',
#                          json=data_dict)

# df = response.json()
# print(df)

# Multiple body parameters
# item = {
#     'name': 'Car',
#     'description': 'Honda',
#     'price': 1000,
#     'tax': 100
# }
# user = {'username': 'minhnhk',
#         'fullname': 'Nguyen Huu Khoa Minh'}

# user_item = {'item': item, 'user': user}
# item_id = 10

# response = requests.put(f'http://127.0.0.1:8000/users/{item_id}',
#                         json=user_item)
# result = response.json()
# print(result)
# print(type(result))


# Singular value in body
item = {
    'name': 'Car',
    'description': 'Honda',
    'price': 1000,
    'tax': 100
}
user = {'username': 'minhnhk',
        'fullname': 'Nguyen Huu Khoa Minh'}

user_item = {'item': item, 'user': user, 'importance': True}
item_id = 10

response = requests.put(f'http://127.0.0.1:8000/users/{item_id}',
                        json=user_item)
result = response.json()
print(result)
print(type(result))


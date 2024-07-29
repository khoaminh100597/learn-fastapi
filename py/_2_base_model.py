from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    joined: date

my_first_user = User(id=1, name="John", joined="2018-07-18")

second_user_data = {
    'id': 2,
    'name': 'Mary',
    'joined': '2024-02-03'
}

"""
    **second_user_data means:
    Pass the keys and values of the second_user_data dict directly as key-value arguments, equivalent to: User(id=2, name="Mary", joined="2024-02-03")
"""

my_second_user = User(**second_user_data)

print(my_first_user)
print(my_second_user)
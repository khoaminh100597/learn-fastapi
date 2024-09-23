from typing import Optional, List, Dict, Set, Tuple, Union

# Add type hints with ":". Type hints help the intellisense of vs code
# At the same point, you try to trigger the autocomplete with Ctrl+Space
# You also get error checks

def say_hi(name: Optional[str]):
    print(f"Hey {name}!")

say_hi(name=None)

# Declaring types: int, float, bool, bytes, dict, list, set, tuple
# Generic types, to declare the types and internal types, use the Python module typing

# List
def process_items(items: List[str]):
    for item in items:
        print(item.capitalize())

process_items(['a', 'b', 'c'])

# Tuple and Set
def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    
    print(items_t, items_s)
    print(type(items_t), type(items_s))

    for item in items_t:
        print(item, type(item))

    for item in items_s:
        print(item, type(item))

    return items_t, items_s

print(process_items((4, 'def', 'abc'), {'a', 'b', 'a', 'd'}))

# Dict
# To define a dict, you pass 2 type parameters, separated by commas.
# The first type parameter is for the keys of the dict.
# The second type parameter is for the values of the dict

def process_items(price: Dict[str, float]):
    for item_name, item_price in price.items():
        print(item_name)
        print(item_price)

# Union, you can declare that a variable can be any of several types, for example, an int or a str
# Avoid using Optional[SomeType]
# Instead use Union[SomeType, None] or we use "|". For example, Union[str, None] equivalent to str | None

def process_item(item: Union[int, None]):
    print(item)

print(process_item(item=2))

# Type hints in Fast API
# Editor support
# Type checks
# Define requirements
# Convert Data
# Document with the API
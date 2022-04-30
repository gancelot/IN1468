"""
    25_map_example.py
    Using Python's map() function.
"""
from random import shuffle


def shuffler(normal_str):
    temp_list = list(normal_str)
    shuffle(temp_list)
    return ''.join(temp_list)


mapobj = map(shuffler, ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
print(list(mapobj))

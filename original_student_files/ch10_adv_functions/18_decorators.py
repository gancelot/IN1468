"""
    18_decorators.py
    Using the functools version of the cache...lru_cache.
"""
from functools import lru_cache


@lru_cache
def func1(*args, **kwargs):
    return f'Calling {func1.__name__} with args: {args} and {kwargs}.'


print(func1(1))
print(func1(1, 2, 3))
print(func1('hello'))
print(func1(1))
print(func1('hello'))
print(func1(1, 2))
print(func1(1, 2, 'hello'))
print(func1(1, val=2, item=3))
print(func1(1, val=2))
print(func1(1, val=2, item=3))
print(func1(1, item=3, val=2))

print(func1.cache_info())
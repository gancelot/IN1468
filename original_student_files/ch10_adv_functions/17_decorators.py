"""
    17_decorators.py

    A function caching decorator.
"""
from functools import wraps

def cache_call(orig_func):
    cache = {}

    @wraps(orig_func)
    def wrapper(*args):
        if args not in cache:
            ret = orig_func(*args)
            cache[args] = ret
            wrapper.misses += 1
        else:
            wrapper.hits += 1

        return cache[args]

    wrapper.hits = 0
    wrapper.misses = 0

    return wrapper


@cache_call
def func1(*args):
    return f'Calling {func1.__name__} with args: {args}'


print(func1(1))
print(func1(1, 2, 3))
print(func1('hello'))
print(func1(1))
print(func1('hello'))
print(func1(1, 2))

print(f'Cache hits: {func1.hits}, cache misses: {func1.misses}')

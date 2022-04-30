"""
    02_decorators.py

    Functions are first order objects in Python.
    This means they can be passed into other functions,
    they can be returned from functions, AND they can be created within functions.

"""

def increment(val, amount):
    return val + amount


def decrement(val, amount):
    return val - amount


def op(func, data, amt):
    result = func(data, amt)
    return result


print(op(increment, 5, 3))
print(op(decrement, 3, 2))

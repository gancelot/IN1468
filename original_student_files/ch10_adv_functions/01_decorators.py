"""
    01_decorators.py

    In Python the name of a function is a reference to that function in memory.

"""


def some_func(val):
    print(val)


some_func('Calling the function.')

another_func = some_func
another_func('Calling the function.')

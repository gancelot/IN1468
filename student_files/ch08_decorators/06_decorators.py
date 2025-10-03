"""
    06_decorators.py

    Another example of a function that returns another function
    (non-decorated, so far)
"""


def shortener(func):
    width = 15
    def wrapper(val):
        val = val[:width] + '...'
        func(val)
    return wrapper


def display(val):
    print(val)


data = 'This is a long string that will be truncated.'
display(data)


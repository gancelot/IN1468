"""
    07_decorators.py

    Before applying the decorator syntax.
    This version performs the function swap...shortener
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
display = shortener(display)
display(data)

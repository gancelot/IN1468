"""
    08_decorators.py

    Here it is..(finally!)...the decorator syntax
"""


def shortener(func):
    width = 15

    def wrapper(val):
        val = val[:width] + '...'
        func(val)
    return wrapper


@shortener
def display(val):
    print(val)


data = 'This is a long string that will be truncated.'
display(data)

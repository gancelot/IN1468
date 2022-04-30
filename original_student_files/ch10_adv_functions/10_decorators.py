"""
    10_decorators.py

    This one will error when we decorate a function with too many args...
"""


def shortener(func):
    width = 15
    def wrapper(val):
        val = val[:width] + '...'
        return func(val)
    return wrapper


@shortener
def display(val):
    print(val)


@shortener
def display_info(name, address):
    print(name, address)

data = 'This is a long string that will be truncated.'
display(data)
display_info('Johnny', '124 Main St.')

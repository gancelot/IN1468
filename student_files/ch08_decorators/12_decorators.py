"""
    12_decorators.py

    Fixing arguments for positional AND keywords
"""


def shortener(func):
    width = 15

    def wrapper(*args, **kwargs):
        arguments = []
        for arg in args:
            if isinstance(arg, str):
                arguments.append(arg[:width])
            else:
                arguments.append(arg)

        key_args = {key: val[:width] for key, val in kwargs.items() if isinstance(val, str)}

        return func(*arguments, **key_args)
    return wrapper


@shortener
def display(val):
    print(val)


@shortener
def display_info(name, address):
    print(name, address)


data = 'This is a long string that will be truncated.'
display(data)
display_info('Kiefer William Frederick Dempsey George Sutherland',
             '123 Chancellor Matheson Road')

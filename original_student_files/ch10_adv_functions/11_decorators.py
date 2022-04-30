"""
    11_decorators.py

    Now we have fixed the arguments issue...(positional only)
"""


def shortener(func):
    width = 15
    def wrapper(*args):
        arguments = []
        for arg in args:
            if isinstance(arg, str):
                arguments.append(arg[:width])
            else:
                arguments.append(arg)
        return func(*arguments)
    return wrapper


@shortener
def display(val):
    print(val)


@shortener
def display_info(name, address):
    print(name, address)

data = 'This is a long string that will be truncated.'
display(data)
display_info('Kiefer William Frederick Dempsey George Sutherland', '123 Chancellor Matheson Road')

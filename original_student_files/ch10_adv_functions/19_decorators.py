"""
    19_decorators.py
    decorating a decorator...
"""


def lowercaser(func):
    def wrapper(*args, **kwargs):
        arguments = []
        for arg in args:
            if isinstance(arg, str):
                arg = arg.lower()
            arguments.append(arg)

        kwargs = {key:val.lower() for key, val in kwargs.items()
                    if isinstance(val, str)}
        return func(*arguments, **kwargs)

    return wrapper


def shortener(func):
    width = 15
    def wrapper(*args, **kwargs):
        arguments = []
        for arg in args:
            if isinstance(arg, str):
                arguments.append(arg[:width])
            else:
                arguments.append(arg)

        key_args = {}
        for key, val in kwargs.items():
            if isinstance(val, str):
                key_args[key] = val[:width]

        return func(*arguments, **key_args)
    return wrapper


@lowercaser
@shortener
def display_info(name, address):
    print(name, address)


display_info('Kiefer William Frederick Dempsey George Sutherland',
             address='123 Chancellor Matheson Road')
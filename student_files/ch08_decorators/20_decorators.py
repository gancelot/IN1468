"""
    20_decorators.py
    Classes as decorators...
"""
from numbers import Number


class check_numeric:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        retval = 'Invalid argument supplied.  Must be numeric.'

        check_args = all(isinstance(arg, Number) for arg in args)
        check_kwargs = all(isinstance(val, Number) for val in kwargs.values())
        if check_args and check_kwargs:
            retval = self.func(*args, **kwargs)

        return retval


@check_numeric
def sum(x, y):
    return f'Result: {x + y}'


print(sum(10, 3.5))
print(sum(0, 'Johnny'))

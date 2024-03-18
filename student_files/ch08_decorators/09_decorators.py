"""
    09_decorators.py
    Our decorator, a little simplified this time.
"""


def decorator(some_func):
    def wrapper(name):
        print('This is the wrapper.')
        return some_func(name)
    return wrapper


@decorator
def display(name):
    print(f'Hi, {name}')


display('Johnny')

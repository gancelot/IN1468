"""
    14_decorators.py

    A function call count decorator.
"""


def count(func):
    call_count = 0

    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f'{func.__name__}, call #{call_count}')
        return func(*args, **kwargs)
    return wrapper


@count
def func1(greeting: str = 'hi, there'):
    print(greeting)


func1('hello')
func1(greeting='howdy')
func1('hey')
func1()

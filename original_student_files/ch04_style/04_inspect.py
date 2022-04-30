from itertools import chain
import inspect


def my_func(a, b=1, c=2, *d, e, f=3, **g) -> list:
    frame = inspect.currentframe()
    args, varargs, varkwargs, locls = inspect.getargvalues(frame)

    print(f'args={args}')
    print(f'varargs={varargs}')
    print(f'varkwargs={varkwargs}')

    return [(i, locls[i]) for i in chain(args, varargs, varkwargs)]


print(f'all results={my_func(10, 20, e=40, x=50)}')

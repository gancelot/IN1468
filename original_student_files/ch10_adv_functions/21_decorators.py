"""
    21_decorators.py
    Decorating a class...
"""


def dec(cls):
    orig_init = cls.__init__
    
    def __init__(self, *args, **kwargs):
        print('doing something before')
        orig_init(self, *args, **kwargs)
        print('doing something after')
        
    cls.__init__ = __init__
    
    return cls


@dec
class Foo(object):
    def __init__(self):
        print('original init')

Foo()
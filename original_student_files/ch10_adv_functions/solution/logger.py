"""
            logger.py   -   Use this module to define a decorator that will be used to
                            decorate the methods of the main module (get_location())
                            to indicate when the methods are called.
"""

import logging
logging.basicConfig(filename='./logfile.log', level=logging.DEBUG)


def log(orig_func):
    def wrapper(*args, **kwargs):
        ret_val = orig_func(*args, **kwargs)
        arguments = []
        for arg in args:
            if not isinstance(arg, str):
                arguments.append(type(arg).__name__)
            else:
                arguments.append(arg)
        for kw, val in kwargs.items():
            if not isinstance(val, str):
                arguments.append(type(val).__name__)
            else:
                arguments.append(f'{kw}={val}')

        logging.info(f'{orig_func.__name__}() called.  Arguments: {" ".join(arguments)}.  Return value: {ret_val}')
        return ret_val
    return wrapper

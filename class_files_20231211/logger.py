"""
            logger.py   -   Use this module to define a decorator that will be used to
                            decorate the methods of the main module (get_location())
                            to indicate when the methods are called.
"""
import logging

logging.basicConfig(level=logging.DEBUG)


def log(func):
    def wrapper(*args, **kwargs):
        ret_val = func(*args, **kwargs)

        logging.info(f'{func.__name__} was called, returned: {len(ret_val)} records.')

        return ret_val

    return wrapper

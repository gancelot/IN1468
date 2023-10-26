"""
            logger.py   -   Use this module to define a decorator that will be used to
                            decorate the methods of the main module (get_location())
                            to indicate when the methods are called.
"""

import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)


def log(func):
    def wrapper(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        params = []
        for arg in args:
            try:
                params.append(str(arg))
            except Exception:
                pass

        params = ', '.join(params)

        logging.info(f'{func.__name__} called. Args passed: {params}')

        return ret_val

    return wrapper


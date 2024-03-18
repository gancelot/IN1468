"""
            logger.py   -   Use this module to define a decorator that will be used to
                            decorate the methods of the main module (get_location())
                            to indicate when the methods are called.
"""

import logging

# Step 1. Establish a basic configuration for the logger (refer to your slides
#         on how to do this).


# Step 2. Write a decorator (using the pattern discussed in the notes) that
#         contains a wrapper function and calls an original function.
#
#                 def log(orig_func):
#                     def wrapper(*args, **kwargs):
#                         ret_val = orig_func(*args, **kwargs)
#
#                         (add logging call here)
#
#                         return ret_val
#                     return wrapper
#
#         It will then also log (use log.info() ) the function call.  Keep the log entry
#         simple, like log.info('Function called.')

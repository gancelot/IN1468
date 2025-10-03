"""
    03_decorators.py

    Another example of a function that returns another function
"""


def display_width(width):
    def display(val):
        print(val[:width] + '...')
    return display


short_formatter = display_width(15)

data = 'This is a long string that will be truncated.'
short_formatter(data)

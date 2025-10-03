"""

    The Python ternary operator and the use of raise <ExceptionType> from <error>

"""


def convert(data):
    value, typ = data if isinstance(data, tuple) else (data, str)
    try:
        return typ(value)
    except Exception as err:
        raise TypeError('Error converting.') from err


test_values = [('16.6', float), 33.7, ('hello', int)]
for value in test_values:
    try:
        result = convert(value)
        print(result, type(result))
    except Exception as err:
        print(err.__cause__)

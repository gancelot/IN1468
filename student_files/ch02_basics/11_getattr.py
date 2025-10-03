"""

    Using getattr()

"""

import sys

_items = []                             # _items gets populated elsewhere


print(getattr(sys, 'version'))          # a simple example of using getattr()


def most(field_name):
    try:
        return max(_items, key=lambda record: getattr(record, field_name))
    except ValueError:
        return None


most('population')

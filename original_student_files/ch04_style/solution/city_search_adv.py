"""
      city_search_adv.py   -   This file is used with task4_1_adv.py

      This module is a revision of the city_search_adv.py from Task3-1.
      This version contains documentation including docstrings and type annotations.
"""
from typing import NamedTuple, Dict, Union, Tuple, TypeVar

_items = []


def read_data(fullname: str, data_fields:Dict=None, sep:str =','):
    """
        This refactored version generically reads data into a named tuple with any field names desired.

        Usage:
            read_data('datafile.csv', data_fields={'colname1': 1, 'colname2': (2, int), ...}, sep=',')
    """
    if not data_fields:
        return

    Record = NamedTuple('Record', data_fields.keys())
    with open(fullname, encoding='utf-8') as f:
        for line in f:
            data_values = line.strip().split(sep)
            desired_values = []                              # keeps only the columns we asked for
            for position in data_fields.values():            # may be 1 or 7 or (13, int) for example
                typ = None
                if isinstance(position, tuple):              # check if data_field item is a tuple (13, int) for example
                    position, typ = position                 # extract the position (col number) and type to convert to
                value = data_values[position]                # this is always a str
                if typ:
                    value = typ(value)                       # dynamically typecasts if a type is specified
                desired_values.append(value)
            record = Record(*desired_values)
            _items.append(record)


def most(field_name):
    """
        Alternative to largest() and highest()
        Usage:
             obj.most('population') or obj.most('highest') or whatever header name is desired
    """
    result = max(_items, key=lambda record: getattr(record, field_name))
    return result


def search(term, by='name'):
    """Performs a search by the search term on the column of choice (def. is 'name')."""
    results = [item for item in _items if term.lower() in getattr(item, by).lower()]
    return results


if __name__ == '__main__':
    import pathlib
    working_dir = '../../resources'
    filename = 'simpsons.csv'
    read_data(pathlib.Path(working_dir) / filename, data_fields={'name': 1, 'actor': 2, 'role': 3})
    print(search('julie', by='actor'))

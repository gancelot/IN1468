"""

    search.py - This is the completed solution for Task 2-5.

"""
import sys
from pathlib import Path
from typing import NamedTuple

_items = []


def read_data(filename, data_fields, sep=','):
    _items.clear()

    attributes = []                                             # create the NamedTuple based on the data_fields provided
    for key, val in data_fields.items():
        typ = val[1] if isinstance(val, tuple) else str         # assume str types unless provided
        attributes.append((key, typ))
    Record = NamedTuple('Record', attributes)

    try:
        with open(Path(filename), encoding='utf-8') as f:
            for line in f:
                data_values = line.strip().split(sep)
                desired_values = []                              # keeps only the columns we asked for
                try:
                    for value in data_fields.values():
                        col_num, typ = (value[0], value[1]) if isinstance(value, tuple) else (value, str)
                        desired_values.append(typ(data_values[col_num]))
                    record = Record(*desired_values)
                    _items.append(record)
                except (TypeError, ValueError):
                    pass
    except IOError as err:
        print(f'Error reading from file. Err: {err}', file=sys.stderr)
        sys.exit(1)


def most(field_name):
    return max(_items, key=lambda item: getattr(item, field_name))


def search(term, by):
    results = [item for item in _items if term.casefold() in getattr(item, by).casefold()]

    if results:
        column_format = ''
        padding = 7
        for i in range(len(results[0]._fields)):
            max_width = max([len(str(record[i])) for record in results])
            column_format += f'{{{i}:<{max_width + padding}}}'              # (example) makes: {1:<17}

        print(column_format.format(*results[0]._fields))
        for item in results:                                                # for simplicity values are left aligned
            print(column_format.format(*item))
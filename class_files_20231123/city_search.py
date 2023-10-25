"""
      city_search.py   -   Refactored task2_3.py solution,
                           used with task3_1_starter.py

      This module is called by task3_1_starter.py.  It reads data from cities15000.txt,
      collects the name, population, elevation, and country code into a NamedTuple.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching cities by name and returning results.
"""
import sys
from collections import namedtuple
from pathlib import Path
from typing import Any


_items = []


def read_data(filepath: str | Path, data_fields: dict = None, sep: str = ',') -> None:
    Record = namedtuple('Record', data_fields.keys())
    filepath = Path(filepath)
    try:
        with filepath.open(encoding='utf-8') as f:
            for line in f:
                fields = line.strip().split(sep)
                desired_fields = []
                for col_num in data_fields.values():
                    typ = None
                    if isinstance(col_num, tuple):
                        idx, typ = col_num
                        value = fields[idx]
                    else:
                        value = fields[col_num]
                    if typ:
                        value = typ(fields[idx])
                    desired_fields.append(value)
                record = Record(*desired_fields)
                _items.append(record)
    except IOError as err:
        print(err, file=sys.stderr)


def most(field: str) -> Any:
    return max(_items, key=lambda record: getattr(record, field))


def search(search_term: str, field: str) -> Any:
    return [item for item in _items if search_term.casefold() in getattr(item, field).casefold()]

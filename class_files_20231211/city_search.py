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
    global _items
    _items = []
    Record = namedtuple('Record', data_fields.keys())
    filepath = Path(filepath)
    try:
        with filepath.open(encoding='utf-8') as f:
            for line in f:
                values = line.strip().split(sep)
                desired_fields = []
                for column_num, typ in data_fields.values():
                    desired_fields.append(typ(values[column_num]))
                record = Record(*desired_fields)
                _items.append(record)
    except Exception as err:
        print(f'An error occurred: {err}.')
        sys.exit(1)


def most(field: str) -> Any:
    return max(_items, key=lambda record: getattr(record, field))


def search(search_val: str, field: str) -> list:
    return [item for item in _items if search_val.casefold() in str(getattr(item, field)).casefold()]

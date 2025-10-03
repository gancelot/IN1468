"""

    search.py - This is the completed solution for Task 2-4.

"""
import sys
from pathlib import Path
from typing import NamedTuple
working_dir = Path('../../../resources')
city_data = working_dir / 'cities15000.txt'
_items = []

header = [('name', str), ('population', int), ('elevation', int), ('country', str)]
Item = NamedTuple('Item', header)

try:
    with city_data.open(encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split("\t")
            name = fields[1]
            country_code = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            _items.append(Item(name, population, elevation, country_code))
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)
    sys.exit(1)


def most(field_name):
    return max(_items, key=lambda item: getattr(item, field_name))


def search(term, by):
    # by using getattr().casefold() this will only work with string types
    results = [item for item in _items if term.casefold() in getattr(item, by).casefold()]

    if results:
        print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*[h[0] for h in header]))
        for item in results:
            print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*item))
    else:
        print('No cities found.')

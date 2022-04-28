"""
      city_search.py   -   Refactored task2_3.py solution,
                           used with task3_1_starter.py

      This module is called by task3_1_starter.py.  It reads data from cities15000.txt,
      collects the name, population, elevation, and country code into a NamedTuple.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching cities by name and returning results.
"""
from pathlib import Path
import sys
from typing import NamedTuple

cities = []

City = NamedTuple('City', [('name', str), ('population', int), ('elevation', int), ('country', str)])


def read_data(filepath: Path):
    try:
        with filepath.open(encoding='utf-8') as f:
            for line in f:
                fields = line.strip().split('\t')
                name = fields[1]
                population = int(fields[14])
                elevation = int(fields[16])
                country = fields[8]
                cities.append(City(name, population, elevation, country))
    except IOError as err:
        print(f'Error: ', err, file=sys.stderr)
        sys.exit()

    return len(cities)


def largest():
    return max(cities, key=lambda city: city.population)


def highest():
    return max(cities, key=lambda city: city.elevation)


def search(name: str):
    return [city for city in cities if name.casefold() in city.name.casefold()]


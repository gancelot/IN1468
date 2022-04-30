"""
      city_search.py   -   Refactored task2_3.py solution,
                           used with task3_1.py

      This module reads data from cities15000.txt, collects the name, population,
      elevation, and country code into a namedtuple.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching city names.

"""
from typing import NamedTuple

_cities = []


def read_data(fullname):
    City = NamedTuple('City', [('name', str), ('population', int), ('elevation', int), ('country', str)])
    with open(fullname, encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            name = fields[1]
            country = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            city = City(name, population, elevation, country)
            _cities.append(city)


def largest():
    return sorted(_cities, key=lambda city: city.population, reverse=True)[0]
    # or use max()
    # return max(_cities, key=lambda city: city.population)


def highest():
    return sorted(_cities, key=lambda city: city.elevation, reverse=True)[0]
    # or use max()
    # return max(_cities, key=lambda city: city.elevation)


def search(name):
    results = []
    for item in _cities:
        if name.casefold() in item.name.casefold():
            results.append(item)
    return results

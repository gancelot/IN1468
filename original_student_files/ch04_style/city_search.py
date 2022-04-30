"""
      city_search.py   -   To be used with task4_1_starter.py

      This module reads data from cities15000.txt, collects the name, population,
      elevation, and country code into a list of namedtuples.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching city names.

      This task requires us to document the provided functions with annotations and
      docstrings.  Do this for the 4 functions below and test it in PyCharm from within
      task4_1_starter.py
"""
from collections import namedtuple

_cities = []


def read_data(fullname):
    City = namedtuple('City', ['name', 'population', 'elevation', 'country'])
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


def highest():
    return sorted(_cities, key=lambda city: city.elevation, reverse=True)[0]


def search(name):
    results = []
    for item in _cities:
        if name.lower() in item.name.lower():
            results.append(item)
    return results

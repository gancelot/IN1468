"""
      city_search.py   -   To be used with task4_1.py

      This module is a revision of the city_search.py from Task3-1.
      This version contains documentation including docstrings and type annotations.
      It also makes use of the typing modules NamedTuple for stricter type checking.

"""
from typing import List, NamedTuple

City = NamedTuple('City', [('name', str), ('population', int),
                           ('elevation', int), ('country', str)])

_cities = []


def read_data(fullname: str) -> None:
    """
    Accepts an absolute or relative path to the data file to be read.
    :param fullname: (str) name and path to the data file.
    :return: None
    """
    with open(fullname, encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            name = fields[1]
            country = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            city = City(name, population, elevation, country)
            _cities.append(city)


def largest() -> City:
    """Returns the largest city based on population from the list of _cities"""
    return max(_cities, key=lambda city: city.population)


def highest() -> City:
    """Returns the highest city based on population from the list of _cities"""
    return max(_cities, key=lambda city: city.elevation)


def search(name: str) -> List[City]:
    """
    Searches the protected _cities names
    :param name: (str) search substring to find within city names
    :return: (list) List of City namedtuples
    """
    results = []
    for item in _cities:
        if name.lower() in item.name.lower():
            results.append(item)
    return results

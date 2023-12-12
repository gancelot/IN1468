"""

      task2_1_starter.py   -   Python Basics Overview

      Reads elevation and population data from resources/cities15000.txt (a tsv file).


      Helpful hints:
      1. Examine the file cities15000.txt.  We will use a sequence to hold City typed NamedTuples
         Create the City typed NamedNuple definition such that it contains a name, population, elevation, and country.
         The population and elevation types will be treated as int types.

      2. Before reading from the file, create a Path() object to the file.

         Do this by wrapping the working_dir in a Path() object and then set city_data to the Path() / filename.
         (e.g., working_dir / 'cities15000.txt')

         Read from the data file into this data structure.  Be sure to use proper error handling
         as discussed in the materials.  The columns you should read are as follows: 1=name, 8=country (2-ltr code),
         14=population, 16=elevation (digital elevation model).  Column 0 is the geonameid.

         Use a 'with' control to open and close the file.

         Read lines from the file.  Each line will become a City typed NamedTuple.
         NOTE: you will need to split on a TAB ('\t') since this file is a tab-separated value file.

         Once complete, you should have a list of City typed NamedTuples.

      3. Verify you have read the file by checking the length of the list of City typed NamedTuples.
"""
from typing import NamedTuple
from pathlib import Path
import sys

working_dir = Path('../resources')
city_data = working_dir / 'cities15000.txt'
cities = []

# part 1:
fields = [('name', str), ('population', int), ('elevation', int), ('country', str)]
City = NamedTuple('City', fields)
try:
    with city_data.open(encoding='utf-8') as f:
        for line in f:
            values = line.strip().split('\t')
            name = values[1]
            country = values[8]
            try:
                population = int(values[14])
                elevation = int(values[16])
                cities.append(City(name, population, elevation, country))
            except ValueError as err:
                pass
except Exception as err:
    print(f'An error occurred: {err}.')
    sys.exit(1)


print(f'{len(cities)} cities read.')


# part 2:
cities.sort(reverse=True, key=lambda city: city.population)
print(f'Largest city: {cities[0].name} with {cities[0].population:,} population.')

cities.sort(reverse=True, key=lambda city: city.elevation)
print(f'Highest city: {cities[0].name} at {cities[0].elevation:,} meters.')

by_population = sorted(cities, key=lambda city: city.population)[-1]
by_elevation = sorted(cities, key=lambda city: city.elevation)[-1]
print(f'Largest: {by_population.name}, highest: {by_elevation.name}')

largest = max(cities, key=lambda city: city.population)
highest = max(cities, key=lambda city: city.elevation)

from prettytable import PrettyTable
p = PrettyTable(City._fields)
p.add_row(largest)
p.add_row(highest)
print(p)


# part 3
def search(search_val: str) -> list[City]:
    return [city for city in cities if search_val.casefold() in city.name.casefold()]


search_value = input('Enter a (partial) city name: ')
results = search(search_value)

print('{0:<35}{1:>18}{2:>18}{3:>15}'.format(*City._fields))
for city in results:
    print(f'{city.name:<35}{city.population:>18,}{city.elevation:>18,}{city.country:>15}')

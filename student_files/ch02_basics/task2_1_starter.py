"""
      task2_1_starter.py   -   Python Basics Overview

      Reads elevation and population data from resources/cities15000.txt (a tsv file).


"""
from typing import NamedTuple
from pathlib import Path
import sys

working_dir = '../resources'
city_data = 'cities15000.txt'
cities = []

# Perform Part 1 here...
City = NamedTuple('City', [('name', str), ('population', int), ('elevation', int), ('country', str)])

filepath = Path(working_dir) / city_data

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

print(f'{len(cities)} cities found.')

cities.sort(key=lambda city: city.population, reverse=True)
print(f'Largest city: {cities[0].name} with population of {cities[0].population:,}')

highest = max(cities, key=lambda city: city.elevation)
print(f'Highest city: {highest.name} at {highest.elevation} meters.')


# Part 3: search() function
def search(name: str):
    return [city for city in cities if name in city.name]


search_name = input('Enter name (or partial name) of a city: ')

print('{0:40}{1:>20}{2:>15}{3:>10}'.format(*City._fields))
for city in search(search_name):
    print(f'{city.name:40}{city.population:>20,}{city.elevation:>15,}{city.country:>10}')



# -----------------------------Task 2-2 Using Pandas----------------------
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

cities_df = pd.read_csv(filepath, sep='\t', usecols=(1, 8, 14, 16), header=None,
                        names=['name', 'country', 'population', 'elevation'])
cities_df.sort_values(by='population', inplace=True, ascending=False)
print(cities_df[:5])

simpsons = pd.read_csv('../resources/simpsons.csv', index_col=0)
print(simpsons.head())

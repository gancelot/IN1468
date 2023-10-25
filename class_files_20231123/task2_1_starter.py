"""

      task2_1-3_starter.py   -   Python Basics Overview

      Helpful hints:
      1. Begin by prompting the user to input a city name (or partial name) to search for

      2. Iterate over the list of cities.  (Lowercase the user's input & the city name)
         While you can use .lower() for this, the preferred method is .casefold().

         Check to see if the user's input is in the city name (use the 'in' operator)
         If it is add it to a list that holds all the matches.
         Note: a list comprehension works nicely here:
         results = [<save city>  <iterate over cities> <check if user input is in city name>]

      3. Display the cities found from the matches (results) in step 2.
"""
import sys
from pathlib import Path
from typing import NamedTuple

from prettytable import PrettyTable

working_dir = '../resources'
city_data = 'cities15000.txt'
cities = []

City = NamedTuple('City', [('name', str), ('population', int), ('elevation', int), ('country', str)])
table = PrettyTable(City._fields)
table.align = 'l'
filepath = Path(working_dir) / city_data
try:
    with filepath.open(encoding='utf-8') as f_cities:
        for line in f_cities:
            fields = line.strip().split('\t')
            try:
                name, population, elevation, country = fields[1], int(fields[14]), int(fields[16]), fields[8]
            except ValueError:
                continue
            city = City(name, population, elevation, country)
            cities.append(city)
            table.add_row(city)
except IOError as err:
    print(err, file=sys.stderr)

print(f'{len(cities)} cities found.')
print(table[:10])

# Task 2-2...
cities.sort(key=lambda city: city.population, reverse=True)
print(f'Largest: {cities[0].name} ({cities[0].population:,})')

cities.sort(key=lambda city: city.elevation, reverse=True)
print(f'Highest: {cities[0].name} ({cities[0].elevation}m)')

city = max(cities, key=lambda city: city.population)
print(f'Largest: {city.name} ({city.population:,})')

city = max(cities, key=lambda city: city.elevation)
print(f'Highest: {city.name} ({city.elevation:}m)')

# ----------------------------------------------------
# Task 2-2 Using Pandas...
import pandas as pd

print('\nUsing Pandas for Task 2-2...')
cities_df = pd.read_csv(filepath, sep='\t', usecols=[1, 8, 14, 16], header=None, encoding='utf-8',
                        names=['city_name', 'country', 'population', 'elevation'])
# print(cities_df.head())
print(f'{cities_df.shape[0]} cities found.')
cities_df.sort_values(by='population', inplace=True)
print(cities_df.iloc[-1].tolist())
print()


# -----------------------------------------------------
# Task 2-3 (Search Function)...
def search(name: str) -> list[City]:
    return [city for city in cities if name.casefold() in city.name.casefold()]


search_name = input('Enter a city name (or partial name) to search for: ')
results = search(search_name)

print('{0:<35}{1:>15}{2:>15}{3:>14}'.format(*City._fields))
for city in results:
    print(f'{city.name:<35}{city.population:>15,}{city.elevation:>15}{city.country:>14}')

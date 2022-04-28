"""
      task3_1_starter.py   -   Modularization

      This file represents the driver for our city_search.py module.

      It reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

import city_search as cs
# import ch03_modularization.city_search as cs

working_dir = '../resources'
data_file = 'cities15000.txt'
fullname = Path(working_dir) / data_file

print(f'{cs.read_data(fullname)} cities found.')

largest = cs.largest()
print(f'Largest city: {largest.name} with population of {largest.population:,}')
highest = cs.highest()
print(f'Highest city: {highest.name} at {highest.elevation} meters.')

search_name = 'New'
print('{0:40}{1:>20}{2:>15}{3:>10}'.format(*cs.City._fields))
for city in cs.search(search_name):
    print(f'{city.name:40}{city.population:>20,}{city.elevation:>15,}{city.country:>10}')


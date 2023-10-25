"""
      task3_1_starter.py   -   Modularization

      This file represents the driver for our city_search.py module.

      It reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

import city_search as cs

working_dir = '../resources'
data_file = 'cities15000.txt'
fullname = Path(working_dir) / data_file

cs.read_data(fullname, data_fields={'name': 1, 'population': (14, int), 'elevation': (16, int)}, sep='\t')

largest = cs.most('population')
print(f'Largest: {largest.name} {largest.population}')
#
highest = cs.most('elevation')
print(f'Highest: {highest.name}')

search_name = input('Enter a search term: ')
results = cs.search(search_name, 'name')

for item in results:
    print(item)

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

cs.read_data(fullname,
             data_fields = {'name': (1, str),
                            'country': (8, str),
                            'population': (14, int),
                            'elevation': (16, int)
                            },
             sep='\t')

print(f'Largest: {cs.most("population").name}')
print(f'Highest: {cs.most("elevation").name}')

search_input = 'los angeles'
results = cs.search(search_input, 'name')

if results:
    print('{0:<35}{1:>18}{2:>18}{3:>15}'.format(*results[0]._fields))
    for city in results:
        print(f'{city.name:<35}{city.population:>18,}{city.elevation:>18,}{city.country:>15}')

cs.read_data('../resources/simpsons.csv',
             {'character': (1, str), 'actor': (2, str), 'role': (3, str)})

search_input = 'simpson'
print(cs.search(search_input, 'character'))

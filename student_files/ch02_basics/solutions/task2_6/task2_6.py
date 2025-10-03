from pathlib import Path

import search

path_dir = Path('../../../resources/')
city_data = 'cities15000.txt'

data_fields = {'name': (1, str), 'population': (14, int), 'elevation': (16, int), 'country': (8, str)}
search.read_data(path_dir / city_data, data_fields, sep='\t')

largest = search.most('population')
highest = search.most('elevation')

print(f'Largest city: {largest.name}, {largest.country} with: {largest.population:,} people')
print(f'Highest city: {highest.name}, {highest.country} at: {highest.elevation} meters ({highest.elevation * 3.28} feet)')

search_term = input('Enter the (partial) name of the city: ')
search.search(search_term, 'name')

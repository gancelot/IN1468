"""
    This version is similar to task2_3.py except that it uses dataclasses instead.
    Note the changed formatting on the output display.

"""
from dataclasses import dataclass, astuple, asdict
from pathlib import Path
import sys

working_dir = Path('../../resources')
city_data = working_dir / 'cities15000.txt'
cities = []


# From Part 1...
@dataclass
class City:
    name: str
    population: int
    elevation: int
    country: str


try:
    with city_data.open(encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            name = fields[1]
            country_code = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            cities.append(City(name, population, elevation, country_code))
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)

print(f'{len(cities)} cities read.')


# Part 2 Solution
largest = sorted(cities, key=lambda city: city.population, reverse=True)[0]
highest = sorted(cities, key=lambda city: city.elevation, reverse=True)[0]

print(f'Largest city: {largest.name}, {largest.country} with: {largest.population:,} people')
print(f'Highest city: {highest.name}, {highest.country} at: {highest.elevation} meters ({highest.elevation * 3.28} feet)')

# Part 2 Using the max() function instead...
print(max(cities, key=lambda city: city.population).name)
print(max(cities, key=lambda city: city.elevation).name)


# Part 3 Adding a search capability...
search = input('Enter the (partial) name of the city: ')
results = [city for city in cities if search.casefold() in city.name.casefold()]
if results:
    print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*asdict(results[0]).keys()))
    for city in results:
        print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*astuple(city)))
else:
    print('No cities found.')


from typing import NamedTuple
from pathlib import Path
import sys

working_dir = Path('../../resources')
city_data = working_dir / 'cities15000.txt'
cities = []

# From Part 1...
header = [('name', str), ('population', int), ('elevation', int), ('country', str)]
City = NamedTuple('City', header)

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
    sys.exit(1)

print(f'{len(cities)} cities read.')


# Part 2 Solution
largest = sorted(cities, key=lambda city: city.population, reverse=True)[0]
highest = sorted(cities, key=lambda city: city.elevation, reverse=True)[0]

print(f'Largest city: {largest.name}, {largest.country} with: {largest.population:,} people')
print(f'Highest city: {highest.name}, {highest.country} at: {highest.elevation} meters ({highest.elevation * 3.28} feet)')


# Part 2 refactored...
print('Part 2 Refactored...')


def largest():
    return max(cities, key=lambda city: city.population)


def highest():
    return max(cities, key=lambda city: city.elevation)


print(f'Largest city: {largest().name}.')
print(f'Highest city: {highest().name}.')


# Part 3 Adding a search capability...
search_term = input('Enter the (partial) name of the city: ')


def search(term):
    results = [city for city in cities if term.casefold() in city.name.casefold()]

    if results:
        print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*[h[0] for h in header]))
        for city in results:
            print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*city))
    else:
        print('No cities found.')


search(search_term)

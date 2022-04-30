"""

      task2_3_starter.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.


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
from typing import NamedTuple
from pathlib import Path
import sys

working_dir = Path('../resources')
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

print(f'{len(cities)} cities read.')

# Part 2 Solution
largest = sorted(cities, key=lambda city: city.population, reverse=True)[0]
highest = sorted(cities, key=lambda city: city.elevation, reverse=True)[0]

# Perform Part 3 here...

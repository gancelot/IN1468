"""

      task2_2_starter.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

      Refer to the steps down below to help complete this task.

"""
from typing import NamedTuple
from pathlib import Path
import sys

working_dir = Path('../resources')
city_data = working_dir / 'cities15000.txt'
cities = []

# Part 1 solution...
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

# Perform Part 2 here...
# Step 1.  To find the largest city, sort the cities data structure by population.
#          The first element in the list will end up being the largest city (a City NamedTuple).
#
#          Tip: As an example of sorting, the following would sort by country:
#                 key=lambda city: city.country


# Step 2. Repeat step 1, this time sorting by elevation instead of population.


# Optional: Can you solve steps 1 & 2 using the max() function instead?
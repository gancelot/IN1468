"""

      task2_3_starter.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

      Refer to the steps listed below to help complete this task.

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
    sys.exit(1)

print(f'{len(cities)} cities read.')

# From Part 2...(these will be replaced in step 5)...
largest = sorted(cities, key=lambda city: city.population, reverse=True)[0]
highest = sorted(cities, key=lambda city: city.elevation, reverse=True)[0]


# Perform Part 3 here...
# Step 1. Begin by prompting the user to input a city name (or partial name) to search for

# Step 2. Create a function that will perform the search functionality.  Have it accept a city name.
#         This function should iterate over the list of city objects and check to see if the search
#         term is within the name.
#
#         Iterate over the list of cities.  (Lowercase the user's input & the city name)
#         You can use .lower() for this but the preferred method is .casefold(). Check to see if the
#         user's input is in the city name (use the 'in' operator).  If it is, add it to a list that
#         holds all the matches.  Note: a list comprehension works nicely here:
#                 results = [<save city>  <iterate over cities> <check if user input is in city name>]


# Step 3. Within your function, print and display the results in a similar fashion to what is shown
#         on the slide.


# Step 4. Invoke the function above passing the search term that the user input.

# Step 5. Refactor the two lines above from Part 2 (lines 39-40) to become functions also.
#         Each should simply take no parameters and should return their sorted (or max) values.
"""
      task3_1_starter.py   -   Modularization

      This file represents the driver for our city_search.py module.

      It reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

# 6.  Add your import to import city_search.py here
#     There are several ways to import, one should work:
#     import ch03_modularization.city_search as cs
#     or use import city_search as cs

working_dir = '../resources'
data_file = 'cities15000.txt'
fullname = Path(working_dir) / data_file

# 7. Call your read_data() function.

# 8. Call your largest() and highest() functions from the other modules.

# 9. Call your search() function passing a partial city name to search for.

# 10. Display your results

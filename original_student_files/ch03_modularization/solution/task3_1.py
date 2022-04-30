"""
      task3_1.py   -   Modularization

      This solution represents a basic solution meeting the requirements.
      For an advanced solution, see task3_1_adv.py.

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

import ch03_modularization.solution.city_search as cs
# or use import city_search as cs

working_dir = '../../resources'
data_file = 'cities15000.txt'

fullname = Path(working_dir) / data_file

cs.read_data(fullname)
print(cs.largest().name)
print(cs.highest().name)

results = cs.search('new')
if not results:
    print('No cities found.')
else:
    for city in results:
        print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*city))



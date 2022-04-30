"""
      task4_1.py   -   Documentation

      This solution works with city_search.py in this folder.
      See city_search.py for the documentation and annotations used in this task.

"""
import os

import ch04_style.solution.city_search as cs

working_dir = '../../resources'
data_file = 'cities15000.txt'

fullname = os.path.join(working_dir, data_file)

cs.read_data(fullname)
print(cs.largest().name)
print(cs.highest().name)

results = cs.search('new')
if not results:
    print('No cities found.')
else:
    for city in results:
        print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*city))



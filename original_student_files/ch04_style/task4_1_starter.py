"""
      task4_1_starter.py   -   Documentation

      This file is a completed version from task3_1.
      It reads data from resources/cities15000.txt (a tsv file) by importing
      and invoking the functions from city_search.py.

      This task asks us to document the functions in the other module,
      city_search.py and then test them from this file using PyCharm (Ctrl-Q)
"""
import os

import ch04_style.city_search as cs

working_dir = '../resources'
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



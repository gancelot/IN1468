"""
      task3_1_adv.py   -   Modularization

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

      The output format is more complicated than the requirements because:
      1) it falls back to standard output if prettytable doesn't exist
      2) it supports supplying any number of columns from the datafile and widths are automatically
         calculated
"""
from pathlib import Path

import ch03_modularization.solution.city_search_adv as cs

working_dir = '../../resources'
datafile = 'cities15000.txt'
data_fields={'name': 1, 'population': (14, int), 'elevation': (16, int), 'country': 8}

fullname = Path(working_dir) / datafile

cs.read_data(fullname, data_fields, sep='\t')
print(cs.most('population').name)
print(cs.most('elevation').name)

results = cs.search('New')

if not results:
    print('No results found.')
else:
    field_headers = results[0]._asdict().keys()                               # fields in the namedtuple
    try:
        from prettytable import PrettyTable                                   # if error, fallback to except clause
        pt = PrettyTable(field_headers)
        pt.align = 'l'                                                        # left align (center is default)
        for item in results:
            pt.add_row(item)
        print(pt)
    except ModuleNotFoundError:                                               # manual formatting
        column_format = ''                                                    # we'll copy prettytable and left-align
        padding = 7
        for i in range(len(field_headers)):                                   # iterate each column
            col_width = max([len(str(item[i])) for item in results])          # find the longest value
            column_format += f'{{{i}:<{col_width + padding}}}'                # (example) makes: {1:<17}
        print(column_format.format(*field_headers))                           # all headers are left-aligned
        for item in results:                                                  # print results all (numbers left-aligned)
            print(column_format.format(*item))

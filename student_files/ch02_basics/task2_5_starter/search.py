"""

    search.py - This is the file to work on for Task 2-5.
                Complete this module by converting the portion of it that reads data from cities15000.txt
                into a generic function called read_data() that can read most data files.

    Helpful hints:

    1. Remove the lines below that create the header and Item NamedTuple.  Also, remove the try-except IOError
       code that reads from cities15000.txt (96-109 below).  You will re-write it in steps 2-5.

       Finally, remove the working_dir and city_data variable declarations below (lines 91-92).  We'll be
       passing these values in via a call to our new function from the other module.


    2. Below the _items declaration, create a function called read data.  Use the signature shown on the slide:

            def read_data(filename, data_fields, sep=','):
                (to be completed next step)


    3. Dynamically create a NamedTuple based on the dictionary passed in (data_fields).  The
       keys are the attributes and the second value in the tuple is the type.  We need the
       attribute and type to create the NamedTuple.  The following will do this:

        _items.clear()

        attributes = []
        for field_name, details in data_fields.items():
            typ = details[1] if isinstance(details, tuple) else str
            attributes.append((field_name, typ))
        Record = NamedTuple('Record', attributes)

        filepath = Path(filename)


       Place these lines in your read_data() function.


    4. Within a 'with' control, read line-by-line from our data file.  strip() and
       split() the fields based on the provided sep value.  Use the following as a template:

        try:
            with open(Path(filepath), encoding='utf-8') as f:
                for line in f:
                    data_values = line.strip().split(sep)
                    ...(to be completed next step)...
        except IOError as err:
            print(f'Error: {err}', file=sys.stderr)
            sys.exit(1)



    5. Complete reading the data into the Record() NamedTuple at the location marked "(to be completed next step)" above.
       For each of the data_fields supplied, get its column number (col) and type (typ).  Perform the type cast.
       Add the value into a list.  Use that list to create the Record NamedTuple.  Add it to our _items.
       (Note: this step is a little tricky!  Feel free to work off of the code provided below)

            data_values = line.strip().split(sep)
            desired_values = []
            try:
                for value in data_fields.values():
                    col_num, typ = (value[0], value[1]) if isinstance(value, tuple) else (value, str)
                    desired_values.append(typ(data_values[col_num]))
                record = Record(*desired_values)
                _items.append(record)
            except (TypeError, ValueError):
                pass

    6. Replace the print statements in the search function.  These were fixed for the
       City NamedTuple.  Now we have variable sized columns.
       Replace the if ... else ... at the bottom of the search() function with
       the following:

           if results:
                column_format = ''
                padding = 7
                for i in range(len(results[0]._fields)):
                    max_width = max([len(str(record[i])) for record in results])
                    column_format += f'{{{i}:<{max_width + padding}}}'

                print(column_format.format(*results[0]._fields))
                for item in results:
                    print(column_format.format(*item))

"""
import sys
from pathlib import Path
from typing import NamedTuple

working_dir = Path('../../resources')
city_data = working_dir / 'cities15000.txt'

_items = []

header = [('name', str), ('population', int), ('elevation', int), ('country', str)]
Item = NamedTuple('Item', header)

try:
    with city_data.open(encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            name = fields[1]
            country_code = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            _items.append(Item(name, population, elevation, country_code))
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)


def most(field_name):
    return max(_items, key=lambda item: getattr(item, field_name))


def search(term, by):
    results = [item for item in _items if term.casefold() in getattr(item, by).casefold()]

    if results:
        print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*[h[0] for h in header]))
        for item in results:
            print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*item))
    else:
        print('No cities found.')

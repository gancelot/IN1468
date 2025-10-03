"""
    search.py - This file should be completed for Task 2-4.

    Refactor the provided task2_4_starter.py as follows:

    1. Move (copy) the largest(), highest() and search() functions from Task 2-3 into this file.
       Note: don't copy the input() statement.


    2. Move the code that reads the data from the file into this module.
       Specifically: move the entire
           try:
               ...
           except IOError:
               ...

       into this file placing it below the City Namedtuple definition.  (You do not need to copy the print statement)


    3. Rename cities to _items -- a more generic name.
       Hint: Within PyCharm, select cities > right-click > Refactor > Rename... > (type the new name).

       Also using the same trick as above, rename City to Item.  (Change the "City" string
       within the NamedTuple to "Item" manually).

       Rename city to item throughout the file.  You will need to do this several times in the file.

       After this step, there should be no reference to City or city throughout the file.
       There should also be no errors in the file at this point.


    4. Combine largest() and highest() to become a single function, called most() that
       accepts the field_name to get the max() for.  Refer to the slide on using getattr()
       to accomplish this.


    5. Modify the search() function definition.  The search_term is already passed in,
       so now pass in a second parameter called "by" that will specify which field to search on.
       Example:
           def search(term, by):
                ...

    6. Modify search() to work with the new 'by' parameter (hint: use getattr() ).
       Do this by iterating each of the _items and for each item, compare the search term
       to see if it is in the value for getattr(item, by).  If so, keep the item.  (Here, item
       is a City NamedTuple, but we are working to make this more generic shortly).


    7. Use the provided task2_4_test.py file to test if your search.py module works.
"""
import sys
from pathlib import Path
from typing import NamedTuple

working_dir = Path('../../resources')
city_data = working_dir / 'cities15000.txt'
cities = []

header = [('name', str), ('population', int), ('elevation', int), ('country', str)]
City = NamedTuple('City', header)

# Place functions here
"""
      city_search.py   -   Refactored task2_3.py solution,
                           used with task3_1_starter.py

      This module is called by task3_1_starter.py.  It reads data from cities15000.txt,
      collects the name, population, elevation, and country code into a NamedTuple.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching cities by name and returning results.
"""
from typing import NamedTuple


# 1. Move your code from task2_3_starter.py that deals with reading file data into
#    this location.  Place this code into a function called read_data() that accepts
#    a filename.  You may wish to define your cities collection (outside of the
#    function).
#    You may also define your City NamedTuple outside the function if you wish.  (It
#    can also be defined inside the read_data() function.


# 2. Define your largest() function.  Define a function called largest and move the
#    code from task2_3_starter.py that dealt with this into this function.
#    This will likely be your max() or sorted() statement.  Don't forget to return the result!

# 3. Repeat step 2, this time for the highest() function.

# 4. Create your search() function.  Have this function accept a parameter for the city name
#    to search for.  Move your search-related code from task2_3_starter.py into this function.

# 5. Clean up any errors and then switch to the task3_1_starter.py file call these functions.

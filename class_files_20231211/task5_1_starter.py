"""

      task5_1_starter.py   -   Python Database API 2.0

      Reads data from the schools table within course_data.db by invoking the get_location()
      function and a partial or full name of a school.

      Data returned from the search of the database returns name, city, and state for all
      matching results.

      Uses a Data Class to store school data.



      Instructions:
      1. Begin by creating a data class.  Refer back to chapter 2 in the notes about data classes
         for specifics on how to create one.  The data class should contain
         fields such as: name, city, and state, and each are strings.

      2. Within the provided get_location function, you should:
         a) Obtain a connection to the database.
         b) Obtain a cursor.
         c) Execute a query.  Use the following SQL to help generate results:

         'SELECT fullname, city, state FROM schools WHERE fullname like ?'

         d) Fetch the records.  In the execute method, you should fill in the question mark with the
            school name as follows: ('%' + school_name + '%',)

         e) Convert the results into a list of School data classes and return the list from get_location.

         Refer to the slide within the student manual entitled "Accessing Data" for
         help with proper db API syntax--including proper exception handling

      3. Prompt the user for a school name, invoke the get_location() function and pass the user's
         input value into it.  Verify it returns expected results and display the results.

"""
import sqlite3
import sys
from contextlib import closing
from dataclasses import dataclass

import click

data_sourcefile = 'course_data.db'
select_schools_sql = 'SELECT fullname, city, state FROM schools WHERE fullname like ?'

@dataclass
class School:
    name: str
    city: str
    state: str

    def __str__(self):
        return self.name + '(str)'

    def __repr__(self):
        return self.name + '(repr)'


def get_location(school_name: str) -> list[School]:
    results = []

    try:
        with closing(sqlite3.connect(data_sourcefile)) as conn:
            cursor = conn.cursor()
            cursor.execute(select_schools_sql, [f'%{school_name}%'])
            for school in cursor:
                results.append(School(*school))
    except sqlite3.Error as err:
        print(f'Error: {err}')

    return results


search_value = click.prompt('Provide a school to search for', default='Colorado')

results = get_location(search_value)
for school in results:
    print(f'{school.name} ({school.city}, {school.state})')

print(results)
print(results[0])

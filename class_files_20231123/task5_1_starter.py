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
from contextlib import closing
from dataclasses import dataclass


data_sourcefile = 'course_data.db'
sql_query = 'SELECT fullname, city, state FROM schools WHERE fullname like ?'


@dataclass
class School:
    name: str
    city: str
    state: str


def get_location(school_name: str) -> list[School]:
    results = []

    with closing(sqlite3.connect(data_sourcefile)) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query, ['%' + school_name + '%'])
        for name, city, state in cursor:
            school = School(name, city, state)
            results.append(school)

    return results


search_name = input('Enter (partial) name of school: ')
results = get_location(search_name)
print(f'Matches for {search_name}:')
for school in results:
    print(f'{school.name} ({school.city}, {school.state})')

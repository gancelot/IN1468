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
from contextlib import closing
from dataclasses import dataclass
import sqlite3
import sys

data_sourcefile = 'course_data.db'


@dataclass
class School:
    name: str
    city: str
    state: str


def get_location(school_name):
    results = []

    with closing(sqlite3.connect(data_sourcefile)) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT fullname, city, state FROM schools WHERE fullname like ?', ['%' + school_name + '%'])

        for sch in cursor:
            results.append(School(*sch))

    return results



records = get_location('loy')
for record in records:
    print(f'{record.name} ({record.city}, {record.state})')

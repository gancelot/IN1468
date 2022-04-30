"""
      task5_1.py   -   Python Database API 2.0

      Reads data from school.db by providing a get_location() function and a partial or full
      name of a school.

      Data returned from the search of the database returns name, city, and state for all
      matching results.

      Uses a Data Class to store school data.

"""
from contextlib import closing
from dataclasses import dataclass
import sqlite3
import sys


@dataclass
class School:
    name: str
    city: str
    state: str


data_sourcefile = 'course_data.db'
SELECT_SCHOOLS_SQL = 'SELECT fullname, city, state FROM schools WHERE fullname like ?'


def get_location(school_name):
    results = []
    try:
        with closing(sqlite3.connect(data_sourcefile)) as conn:
            cursor = conn.cursor()
            cursor.execute(SELECT_SCHOOLS_SQL, ('%' + school_name + '%',))
            for sch in cursor:
                results.append(School(*sch))
    except sqlite3.Error as err:
        print(f'Error working with database: {err}', file=sys.stderr)
    return results


search_name = input('School name (or partial name): ')
results = get_location(search_name)

print(f'Matches for {search_name}:')
for school in results:
    print(f'{school.name} ({school.city}, {school.state}))')

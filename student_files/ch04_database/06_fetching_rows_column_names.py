"""

    06_fetching_rows_column_names.py

    The following changes the row factory used from tuples to Row objects.  These objects can access
    results using column names instead of positions.

"""
from contextlib import closing
import sqlite3

state = 'CO'

with closing(sqlite3.connect('course_data.db')) as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT fullname, city, state FROM schools WHERE state=?', (state,))
    for sch in cursor:
        print(f'{sch["fullname"]} ({sch["city"]}, {sch["state"]})')

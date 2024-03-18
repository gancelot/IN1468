"""

    03_fetching_rows.py

    The following source will create a namedtuple called School.
    It then retrieves rows of data from course_data.db from our student_files

"""
import sqlite3
import sys

state = 'CO'
conn = None
try:
    conn = sqlite3.connect('course_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT fullname, city, state FROM schools WHERE state=?', (state,))

    print(cursor.fetchone())
    print(cursor.fetchmany(size=3))

    for sch in cursor:
        print(f'Name: {sch[0]}, ({sch[1]}, {sch[2]})')

except sqlite3.Error as err:
    print(f'Error: {err}', file=sys.stderr)
finally:
    if conn:
        conn.close()



# Iterating with fetchmany()...
conn = None
page_size = 10
try:
    conn = sqlite3.connect('course_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT fullname, city, state FROM schools')
    records = cursor.fetchmany(size=page_size)
    while records:
        # process 'page_size' records at a time,
        # a generator could yield records, but we haven't
        # learned generators yet
        print(f'{len(records)} records processed.')
        records = cursor.fetchmany(size=page_size)
finally:
    if conn:
        conn.close()

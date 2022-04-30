"""
    04_inserting_with.py
    The example shows how the with control is used with SQLite.
"""
import sqlite3
import sys

data = (110, 'Amber Willis', 3200.0, 0.025, 'C')

# the with control in SQLite is transaction-based
try:
    with sqlite3.connect('course_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO accounts(id, name, balance, rate, acct_type) VALUES (?,?,?,?,?)', data)
        print('Record inserted into accounts')
except sqlite3.Error as err:
    print('Record not inserted into accounts', file=sys.stderr)
    print(f'Error: {err}', file=sys.stderr)
finally:
    if conn:
        conn.close()

# a subsequent transaction removes the record...
try:
    with sqlite3.connect('course_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM accounts WHERE id=110')
        print('Record removed from accounts')
except sqlite3.Error as err:
    print('Record not removed from accounts', file=sys.stderr)
    print(f'Error: {err}', file=sys.stderr)
finally:
    if conn:
        conn.close()

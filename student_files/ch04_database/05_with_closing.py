"""
    05_with_closing.py
    The example shows how sqlite3 can be adapted to close connections
    instead of manage the transaction.
"""
from contextlib import closing
import sqlite3
import sys

data = (110, 'Amber Willis', 3200.0, 0.025, 'C')

# sqlite3 adapted to close connection after the insert operation
with closing(sqlite3.connect('course_data.db')) as conn:
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO accounts(id, name, balance, rate, acct_type) VALUES (?,?,?,?,?)', data)
        print('Record inserted into accounts')
        conn.commit()
    except sqlite3.Error as err:
        conn.rollback()
        print('Record not inserted into accounts', file=sys.stderr)
        print(f'Error: {err}', file=sys.stderr)

# sqlite3 adapted to close connection after the delete operation
with closing(sqlite3.connect('course_data.db')) as conn:
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM accounts WHERE id=110')
        print('Record removed from accounts')
        conn.commit()
    except sqlite3.Error as err:
        conn.rollback()
        print('Record not removed from accounts', file=sys.stderr)
        print(f'Error: {err}', file=sys.stderr)

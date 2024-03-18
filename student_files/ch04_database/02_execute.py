"""

    02_execute.py

"""
import sqlite3
import sys

database_name = 'course_data.db'
table = 'accounts'
DROP_ACCOUNTS_SQL = f'DROP TABLE IF EXISTS {table}'
CREATE_ACCOUNTS_SQL = f'CREATE TABLE IF NOT EXISTS {table} (id VARCHAR(10) NOT NULL PRIMARY KEY, name VARCHAR(150), balance FLOAT, rate FLOAT, acct_type VARCHAR(5))'
INSERT_RECORD = f'INSERT INTO {table}(id,name,balance,rate,acct_type) VALUES (?,?,?,?,?)'


data = [(100, 'John Smith', 5500.0, 0.025, 'C'),
        (101, 'Sally Jones', 6710.11, 0.025, 'C'),
        (102, 'Fred Green', 2201.73, 0.035, 'S'),
        (103, 'Ollie Engle', 187.30, 0.025, 'S'),
        (104, 'Gomer Pyle', 12723.10, 0.015, 'C')]


connection = None
try:
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(DROP_ACCOUNTS_SQL)
    cursor.execute(CREATE_ACCOUNTS_SQL)
    cursor.executemany(INSERT_RECORD, data)
    connection.commit()
    print(f'Data loaded into {table}')
except sqlite3.Error as err:
    if connection:
        connection.rollback()
    print(f'Data not loaded into {table}')
    print(f'Error: {err}', file=sys.stderr)
finally:
    if connection:
        connection.close()

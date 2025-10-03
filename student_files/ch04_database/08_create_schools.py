"""

    08_create_schools.py

    The following source will create (and destroy any previous) tables related
    to the school data loaded from schools.csv.

    At any time this file can be run to re-establish a fresh version of the
    database.  It should create a database file called course_data.db.

"""
import csv
import sqlite3

data_sourcefile = '../resources/baseball/schools.csv'
DROP_SCHOOLS_SQL = 'DROP TABLE IF EXISTS schools'
CREATE_SCHOOLS_SQL = 'CREATE TABLE IF NOT EXISTS schools (school_id VARCHAR(30) NOT NULL PRIMARY KEY, fullname VARCHAR(50), city VARCHAR(50), state VARCHAR(15), country VARCHAR(50))'
INSERT_RECORD = 'INSERT INTO schools(school_id, fullname, city, state, country) VALUES (?,?,?,?,?)'


# read data from the file into a list of records
school_data = []
try:
    with open(data_sourcefile, encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                school_data.append(row)
        except csv.Error as err:
            print(f'Error: {err}')
except IOError as err:
    print(err)


school_data = school_data[1:]
connection = None
try:
    connection = sqlite3.connect('course_data.db')
    cursor = connection.cursor()
    cursor.execute(DROP_SCHOOLS_SQL)
    cursor.execute(CREATE_SCHOOLS_SQL)
    cursor.executemany(INSERT_RECORD, school_data)
    connection.commit()
    print('Data loaded into schools table')
except sqlite3.Error as err:
    if connection:
        connection.rollback()
        print('Data not loaded into schools table')
    print(f'Error: {err}')
finally:
    if connection:
        connection.close()

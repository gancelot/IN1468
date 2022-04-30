"""

    Run as follows:

    09_argparse2.py -n John Smith -m

"""
import argparse
from contextlib import closing
import sqlite3
import sys

db_filename = '../resources/course_data.db'


class School:
    def __init__(self, school_id: str, fullname: str, city: str, state: str, country: str):
        self.school_id = school_id
        self.fullname = fullname
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f'{self.fullname} ({self.city}, {self.state})'

    __repr__ = __str__


def find(value: str = None, column: str = 'fullname', sort_by: str = 'fullname'):
    SELECT_SCHOOLS_SQL = 'SELECT school_id, fullname, city, state, country FROM schools WHERE column like ?'
    PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']

    results = []
    error_msg = ''

    if column not in PERMITTED_SEARCH_COLUMNS:
        error_msg = 'Column not allowed.'
    elif sort_by not in PERMITTED_SEARCH_COLUMNS:
        error_msg = 'Sort (sort_by) field not allowed.'
    else:
        SELECT_SCHOOLS_SQL = SELECT_SCHOOLS_SQL.replace('column', column)

        with closing(sqlite3.connect(db_filename)) as conn:
            print('Database connection opened!')
            cursor = conn.cursor()
            params = ('%' + value + '%',)

            print('Querying...')
            cursor.execute(SELECT_SCHOOLS_SQL, params)

            for record in cursor:
                results.append(School(*record))

            results.sort(key=lambda s: vars(s).get(sort_by))
            print('Database connection closed!')

    return results, error_msg


def get_args():
    parser = argparse.ArgumentParser(description='Personal characteristics')
    parser.add_argument('-v', '--value', nargs='*', required=True)
    parser.add_argument('-c', '--column', default='fullname')
    parser.add_argument('-s', '--sort_by', default='fullname')
    parser.add_argument('-e', '--show_error', action='store_true')

    return parser.parse_args()


args = get_args()
results, error_msg = find(' '.join(args.value), args.column, args.sort_by)
if results:
    print(results)
elif args.show_error:
    print(error_msg, file=sys.stderr)

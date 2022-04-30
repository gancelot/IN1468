"""
    schools.py - This is the solution to Task 6-1 provided as a stand-alone module.
"""
from contextlib import closing
import sqlite3


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


class SchoolManager:
    SELECT_SCHOOLS_SQL = 'SELECT school_id, fullname, city, state, country FROM schools WHERE column like ?'
    PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']

    def __init__(self, db_filename):
        self.db_filename = db_filename

    def find(self, value: str = None, column: str = 'fullname', sort_by: str = 'fullname'):
        """
        Searches the schools table in the database.
        :param value: the search term to perform a partial search for
        :param column: the column to search on (def. is fullname column)
        :param sort_by: the column to sort on (def. is fullname)
        :return: a list of Schools is returned
        """
        results = []
        error_msg = ''

        if not value:
            error_msg = 'Search value parameter must be supplied.'
        elif column not in self.PERMITTED_SEARCH_COLUMNS:
            error_msg = 'Column not allowed.'
        elif sort_by not in self.PERMITTED_SEARCH_COLUMNS:
            error_msg = 'Sort (sort_by) field not allowed.'
        else:
            self.SELECT_SCHOOLS_SQL = self.SELECT_SCHOOLS_SQL.replace('column', column)

            with closing(sqlite3.connect(self.db_filename)) as conn:
                print('Database connection opened!')
                cursor = conn.cursor()
                params = ('%' + value + '%',)

                print('Querying...')
                cursor.execute(self.SELECT_SCHOOLS_SQL, params)

                for record in cursor:
                    results.append(School(*record))

                results.sort(key=lambda s: vars(s).get(sort_by))
                print('Database connection closed!')

        return results, error_msg


if __name__ == '__main__':
    print(SchoolManager('course_data.db').find('Loyola', column='fullname'))
    print(SchoolManager('course_data.db').find('ID', column='state', sort_by='fullname'))

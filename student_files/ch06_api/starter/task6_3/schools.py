"""
    starter/task6_3/schools.py  -   Module for the School and SchoolManger classes

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

    def find(self, value: str, column: str = 'fullname', sort_by: str = 'fullname') -> list[School]:
        results = []

        if column in self.PERMITTED_SEARCH_COLUMNS:                 # only certain, checked columns may be searched
            select_schools_sql = self.SELECT_SCHOOLS_SQL.replace('column', column)

            with closing(sqlite3.connect(self.db_filename)) as conn:
                print('connection opened!')
                cursor = conn.cursor()
                params = (f'%{value}%',)

                print('querying...')
                cursor.execute(select_schools_sql, params)

                for record in cursor:
                    results.append(School(*record))

                print('connection closed!')

            if sort_by in self.PERMITTED_SEARCH_COLUMNS:
                results.sort(key=lambda s: vars(s).get(sort_by))

        return results


if __name__ == '__main__':
    print(SchoolManager('course_data.db').find('Loyola', column='fullname'))
    print(SchoolManager('course_data.db').find('ID', column='state', sort_by='city'))

"""
    task6_1_starter.py  -   Module for the School and SchoolManger classes

    Class module for our School and SchoolManager classes.
"""
from contextlib import closing
import sqlite3


class School:
    def __init__(self, school_id, fullname, city, state, country):
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

    def __init__(self, filepath: str):
        self.filepath = filepath

    def find(self, value: str, column:str = 'fullname', sort_by: str = 'fullname'):
        results = []

        if column not in self.PERMITTED_SEARCH_COLUMNS:
            return results

        self.SELECT_SCHOOLS_SQL = self.SELECT_SCHOOLS_SQL.replace('column', column)

        with closing(sqlite3.connect(self.filepath)) as conn:
            cursor = conn.cursor()
            cursor.execute(self.SELECT_SCHOOLS_SQL, ('%' + value + '%', ))

            for sch in cursor:
                results.append(School(*sch))

            results.sort(key=lambda school: vars(school).get(sort_by, 'fullname'))

        return results


def display_results(results: list):
    """
        Takes a list of objects, displays them in a prettytable
        unless prettytable doesn't exist
    """
    if not results:
        print('Empty results.')
        return

    from prettytable import PrettyTable
    header = vars(results[0]).keys()
    pt = PrettyTable(header)
    pt.align = 'l'
    for item in results:
        pt.add_row(vars(item).values())
    print(pt)


# test your solution out by running the code below and verifying that it works
if __name__ == '__main__':
    # print(SchoolManager('course_data.db').find('Loyola'))
    # print(SchoolManager('course_data.db').find('Loyola', column='fullname'))
    display_results(SchoolManager('course_data.db').find('CO', column='state', sort_by='city'))
    # # testing some unexpected values...
    # print(SchoolManager('course_data.db').find('ID', column='foo', sort_by='fullname'))
    # print(SchoolManager('course_data.db').find('ID', column='fullname', sort_by='foo'))
    display_results(SchoolManager('course_data.db').find('ID', column='foo', sort_by='foo'))
    # print(SchoolManager('course_data.db').find(None, column='foo', sort_by='foo'))

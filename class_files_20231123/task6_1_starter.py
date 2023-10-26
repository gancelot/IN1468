"""
    task6_1_starter.py  -   Module for the School and SchoolManger classes

    Class module for our School and SchoolManager classes.

    The School class simply holds information about school data.
    The SchoolManager is used to connect to and query against
    the course_data.db sqlite3 database.

    -------------------------------------------------------------------------

    Helpful Hints:
    1. Create the School class with the following attributes:
        school_id, fullname, city, state, country

    2. In the __init__, pass in parameters for each and set them as instance attributes


    -------


    3. Create the SchoolManager class beneath School.  Define two methods:
        __init__() and find()

        Remember each method should have a self passed in.

        For now, just put a 'pass' statement in the body of each method.



    4. Complete the __init__() by passing into it the name of the database file
       that we are working with (course_data.db).  Save the filename as an
       attribute in the self object (e.g., self.name = name)



    5. The find() method should accept 3 arguments: the search term,
       the column to search on, and the column to sort on.  Here's
       a possible way to define it:

       def find(self, value, column, sort_by):
           pass



    6. Implement the find() method.

       Connect to and work with the database in a similar fashion
       as you did in task5_1_starter.py.

       You may use the following sql (you can optionally define it in the class outside of any methods):
            SELECT_SCHOOLS_SQL = 'SELECT school_id, fullname, city, state, country FROM schools WHERE column like ?'


       * Note the WHERE clause! The column name in the WHERE clause is variable.  But you
       * can't make this a question mark (?) due to SQL injection concerns.

       * You can however replace the word 'column' using the string class' replace() method.  But you
       * can only replace it with an approved list of columns names, you can't replace it with
       * user input.

       * The following code can be used to insert the variable column name:

       PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']   # place at the class level

       # in find():
       if column in self.PERMITTED_SEARCH_COLUMNS:
            self.SELECT_SCHOOLS_SQL = self.SELECT_SCHOOLS_SQL.replace('column', column)


	   As done in the get_location() method of task5_1_starter.py, connect to, query,
	   and build a list of School objects from the database.



    7. Sort your results based on the provided sort_by value.  You can use the
       following to help:

               results.sort(key=lambda s: vars(s).get(sort_by))

       This converts the school object, s, into a dictionary and then sorts on
       the desired key of that dictionary.



    8. Don't forget to return your results from the find() function

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

    def __repr__(self):
        return f'{self.fullname}'


class SchoolManager:
    SELECT_SCHOOLS_SQL = 'SELECT school_id, fullname, city, state, country FROM schools WHERE column like ?'
    PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']

    def __init__(self, db_file: str):
        self.db_file = db_file

    def find(self, search_term: str, column: str = 'fullname', sort_by: str = 'fullname') -> list[School]:
        results = []

        if column in self.PERMITTED_SEARCH_COLUMNS:
            self.SELECT_SCHOOLS_SQL = self.SELECT_SCHOOLS_SQL.replace('column', column)

            with closing(sqlite3.connect(self.db_file)) as conn:
                cursor = conn.cursor()
                cursor.execute(self.SELECT_SCHOOLS_SQL, ['%' + search_term + '%'])
                for school in cursor:
                    results.append(School(*school))

                if sort_by in self.PERMITTED_SEARCH_COLUMNS:
                    results.sort(key=lambda sch: getattr(sch, sort_by))

        return results


if __name__ == '__main__':
    results = SchoolManager('course_data.db').find('Loyola', column='fullname')
    print(SchoolManager('course_data.db').find('ID', column='state', sort_by='fullname'))
    print(SchoolManager('course_data.db').find('ID', column='state', sort_by='foo'))

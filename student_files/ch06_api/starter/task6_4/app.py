"""
    ch06_api/starter/task6_4/app.py
    This solution combines both SQLAlchemy and Marshmallow with Flask to
    serve up API requests that can search for US-based universities on a
    specified column and sorted by a specified column.  Marshmallow makes it
    easy to return objects in JSON form.

    ****
    Note: before running this server, ensure the previous server (from Task 6-3 or Task 6-1)
    has been shutdown.  In PyCharm, do this by selecting the red square on the tab at the bottom
    of PyCharm in the Run View entitled "app.py"
    ****

"""
from pathlib import Path
from flask import Flask, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db_location = Path(__file__).parent / 'course_data.db'
print(f'Using database at location: {str(db_location)}')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_location)
app.config['SQLALCHEMY_ECHO'] = True

# Step 1. The path to the database file has been provided above.  It has then been supplied
#         to the Flask config dictionary under the key of 'SQLALCHEMY_DATABASE_URI'.  Now,
#         couple the SQLAlchemy and Marshmallow plugins to Flask by passing the app object into
#         each of them.


PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']

# Step 2. To save time, uncomment the class below.
#         Complete the inheritance for the School class below such that it inherits from
#         db.Model
# class School:
#     __tablename__ = 'schools'
#     school_id = db.Column(db.String(40), primary_key=True)
#     fullname = db.Column(db.String(40))
#     city = db.Column(db.String(40))
#     state = db.Column(db.String(40))
#     country = db.Column(db.String(40))
#
#     def __init__(self, school_id: str, fullname: str, city: str, state: str, country: str):
#         self.school_id = school_id
#         self.fullname = fullname
#         self.city = city
#         self.state = state
#         self.country = country
#
#     def __str__(self):
#         return f'{self.fullname} ({self.city}, {self.state})'
#
#     __repr__ = __str__


@app.route('/')
def main_page():
    return redirect('/api/schools/loyola'), 302


@app.route('/api/schools/<search_val>', methods=['GET'])
def get_schools(search_val: str):
    column = request.args.get('column') or 'fullname'
    sort_by = request.args.get('sort_by') or 'fullname'
    if column in PERMITTED_SEARCH_COLUMNS and sort_by in PERMITTED_SEARCH_COLUMNS:
        try:
            # Step 4. Add the SQLAlchemy Query in the space below.  This query will be an
            #         object-oriented version of SQL.  It should take the following structure:
            # schools = db.session.execute(db.select(School)
            #                                          .filter(getattr(School, column).ilike(f'%{search_val}%'))
            #                                          .order_by(getattr(School, sort_by))
            #                                          ).scalars()
            #  The newer SQLAlchemy syntax is referenced like this:
            #             db.session.execute(db.select(Model).filter(Model.attr)
            #  however, here we don't know the column or sort_by values ahead of time.

            # Take the schools obtained from above and pass them into the marshmallow dump() call below
            # to convert them into a list of School objects

            results = school_schema.dump()

            status = 200                                    # 404 = not found
        except Exception as err:
            results = err.args
            status = 404                                    # bad request
    else:
        results=['Invalid column specified.']
        status = 400

    return jsonify(schools=results, search_val=search_val), status


# Step 3.   Remove the pass within the class below.  Have the class inherit from the plugin's
#           main class (ma.Schema).
#           Complete the marshmallow SchoolSchema class.  Using a nested class, called Meta,
#           identify the fields that will be returned to the client.
#           Example:
#           class Meta:
#                 fields = ('school_id', 'fullname', 'city', 'state', 'country')
class SchoolSchema:
    pass


school_schema = SchoolSchema(many=True)

app.run(host='localhost', port=8051)

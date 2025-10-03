"""
    ch06_api/solution/task6_4/app.py
    This solution combines both SQLAlchemy and Marshmallow with Flask to
    serve up API requests that can search for US-based universities on a
    specified column and sorted by a specified column.  Marshmallow makes it
    easy to return objects in JSON form.

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

db = SQLAlchemy(app)
ma = Marshmallow(app)

PERMITTED_SEARCH_COLUMNS = ['fullname', 'city', 'state', 'country']


class School(db.Model):
    __tablename__ = 'schools'
    school_id = db.Column(db.String(40), primary_key=True)
    fullname = db.Column(db.String(40))
    city = db.Column(db.String(40))
    state = db.Column(db.String(40))
    country = db.Column(db.String(40))

    def __init__(self, school_id: str, fullname: str, city: str, state: str, country: str):
        self.school_id = school_id
        self.fullname = fullname
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f'{self.fullname} ({self.city}, {self.state})'

    __repr__ = __str__


@app.route('/')
def main_page():
    return redirect('/api/schools/loyola'), 302


@app.route('/api/schools/<search_val>', methods=['GET'])
def get_schools(search_val: str):
    column = request.args.get('column') or 'fullname'
    sort_by = request.args.get('sort_by') or 'fullname'
    if column in PERMITTED_SEARCH_COLUMNS and sort_by in PERMITTED_SEARCH_COLUMNS:
        try:
            schools = db.session.execute(db.select(School)
                                         .filter(getattr(School, column).ilike(f'%{search_val}%'))
                                         .order_by(getattr(School, sort_by))
                                         ).scalars()

            results = school_schema.dump(schools)
            status = 200
        except Exception as err:
            results = err.args
            status = 404                                                        # Not found
    else:
        results=['Invalid column specified.']
        status = 400

    return jsonify(schools=results, search_val=search_val), status


class SchoolSchema(ma.Schema):
    class Meta:
        fields = ('school_id', 'fullname', 'city', 'state', 'country')


school_schema = SchoolSchema(many=True)

app.run(host='localhost', port=8051)

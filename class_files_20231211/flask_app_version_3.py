from pathlib import Path
from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db_location = Path(__file__).parent / 'course_data.db'
print(str(db_location))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_location)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db  = SQLAlchemy(app)
ma = Marshmallow(app)


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


@app.route('/api/schools/<school_name>', methods=['GET'])
def get_schools(school_name: str):
    try:
        schools = School.query.filter(School.fullname.ilike(f'%{school_name}%')).all()
        results = school_schema.dump(schools)
        status = 404 if schools is None else 200        # 404 = not found
    except Exception as err:
        results = err.args
        status = 400        # bad request

    return jsonify(results=results, school_name=school_name), status


class SchoolSchema(ma.Schema):
    class Meta:
        fields = ('school_id', 'fullname', 'city', 'state', 'country')


school_schema = SchoolSchema(many=True)

app.run(host='localhost', port=8051)

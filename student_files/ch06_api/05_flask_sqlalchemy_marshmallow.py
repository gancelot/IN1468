"""
    05_flask_sqlalchemy_marshmallow.py
    Repeats the previous example, but adds the Marshmallow serialization framework.

    Test this in a browser using:  http://localhost:8051/api/airports/LAX

"""
from datetime import datetime, timedelta, timezone

from pathlib import Path
from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

db_location = Path(__file__).parents[1] / 'resources/course_data.db'
print(f'Using database at location: {str(db_location)}')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_location)
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Airport(db.Model):
    __tablename__ = 'airports'
    airport_id = db.Column('airportid', db.String(10), primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(15))
    abbr = db.Column('IATA_FAA', db.String(50))
    timezone = db.Column('timezone', db.String(50))

    def __init__(self, airport_id: str, name: str, city: str, country: str, abbr: str, timezone: str):
        self.airport_id = airport_id
        self.name = name
        self.city = city
        self.country = country
        self.abbr = abbr
        self.timezone = timezone

    def _get_local_time(self):
        local_time = datetime.now(timezone.utc) + timedelta(hours=float(self.timezone))
        return local_time.strftime('%I:%M%p')

    def __str__(self):
        return f'Local time at {self.name} ({self.city}, {self.country}) is {self._get_local_time()}.'

    def __repr__(self):
        return self.abbr


@app.route('/')
def main_page():
    return redirect('/api/airports/LHR'), 302


@app.route('/api/airports/<search_val>', methods=['GET'])
def get_airport(search_val: str):
    try:
        result = db.session.execute(db.select(Airport).filter_by(abbr=search_val)).scalar_one()
        return jsonify(result=airport_schema.dump(result), localtime=str(result)), 200
    except Exception as err:
        return jsonify(result=err.args[0]), 404


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error=str(error)), 404


class AirportSchema(ma.Schema):
    class Meta:
        fields = ('airport_id', 'name', 'city', 'country', 'abbr', 'timezone')


airport_schema = AirportSchema()

app.run(host='localhost', port=8051)

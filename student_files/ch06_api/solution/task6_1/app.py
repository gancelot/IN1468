"""
    ch06_api/solution/task6_1/app.py -
    This is the Flask server to run.  You will need to run this server and
    then go to your browser and browse to localhost:8051

"""

from flask import Flask, render_template, jsonify, Response
from schools import SchoolManager

app = Flask(__name__)
database = 'course_data.db'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/api/schools/<school_name>', methods=['GET'])
def get_schools(school_name: str) -> Response:
    try:
        results = [str(school) for school in SchoolManager(database).find(school_name)]
    except Exception as err:
        results = err.args

    return jsonify(schools=results, school_name=school_name)


app.run(host='localhost', port=8051)

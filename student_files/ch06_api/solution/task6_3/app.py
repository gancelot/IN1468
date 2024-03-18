"""
    ch06_api/solution/task6_3/app.py -

    This server will be modified to support receiving request parameters.
    Those parameters should be used to modify the query to the database.

    Note: before starting this server, ensure the previous server (from Task 6-1)
    is shutdown

"""

from flask import Flask, render_template, jsonify, Response, request
from schools import SchoolManager

app = Flask(__name__)
database = 'course_data.db'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/api/schools/<search_val>', methods=['GET'])
def get_schools(search_val: str) -> Response:
    search_column = request.args.get('column')
    sort_by = request.args.get('sort_by')
    try:
        results = [str(school)
                   for school in SchoolManager(database).find(search_val, column=search_column, sort_by=sort_by)]
    except Exception as err:
        results = err.args

    return jsonify(schools=results, school_name=search_val)


app.run(host='localhost', port=8051)

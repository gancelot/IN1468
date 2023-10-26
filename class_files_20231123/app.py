"""

    app.py    -   This is the Flask server to run.  You
                  will need to run this server and then go to your
                  browser and browse to localhost:8051


    To get it working properly, however, requires 4 steps to be
    accomplished first:


    1. import the SchoolManager class and call its find() method.
       Can you do this on your own?  If not, refer to the back of the
       student manual


    Perform steps 2 through 4 as described below.

"""

from flask import Flask, render_template, jsonify, Response, request

from schools import SchoolManager

app = Flask(__name__)
database = 'course_data.db'


@app.route('/')
def main_page():
    return render_template('index.html')


# http://localhost:8051/school/Loyola?column=state&sort_by=fullname
@app.route('/school/<school_name>', methods=['GET'])
def get_schools(school_name):
    column = request.args.get('column', 'fullname')
    sort_by = request.args.get('sort_by', 'fullname')
    try:
        schools = SchoolManager(database).find(school_name, column, sort_by)
        results = [str(school) for school in schools]
    except Exception as err:
        results = err.args

    json_response = jsonify(school_name=school_name, schools=results, greet='hello')
    print(json_response.data)
    return json_response


app.run(host='localhost', port=8051)
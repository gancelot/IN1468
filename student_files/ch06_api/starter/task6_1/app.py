"""

    app.py    -   This is the Flask server to run.  You
                  will need to run this server and then go to your
                  browser and browse to localhost:8051


    To get it working properly, however, requires 4 steps to be
    accomplished first:


    1. import the SchoolManager class and call its find() method.
       Can you do this on your own?  If not, refer to the back of the
       student manual


    Perform steps 2 and 3 as described below.

"""

from flask import Flask, render_template, jsonify, Response
# 1. import the SchoolManager class from schools.py here

app = Flask(__name__)
database = 'course_data.db'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/api/schools/<school_name>', methods=['GET'])
def get_schools(school_name: str) -> Response:
    try:
        pass
        # 2. Remove the pass statement above.
        #    Instantiate the SchoolManager and call its find() method
        #    Convert the returned list of School objects into a list
        #    of strings and store this list in the results variable.
        #    An easy way to to this is to iterate over the returned
        #    values from find() and pass them into str() since the
        #    School's __str__ method has been implemented.

    except Exception as err:
        results = err.args

    # 3. Complete the call to jsonify() below.
    #    Pass into jsonify() the school_name (school_name=school_name)
    #    and also pass the list of strings obtained in step 2 above (or results from the Exception)
    #    (schools=results)
    #    set the variable called resp to the return from jsonify()

    resp = jsonify()
    return resp


app.run(host='localhost', port=8051)

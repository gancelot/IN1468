"""
    ch06_api/starter/task6_3/app.py -

    This server will be modified to support receiving request parameters.
    Those parameters should be used to modify the query to the database.

    ****
    Note: before starting this server, ensure the previous server (from Task 6-1)
    is shutdown.  In PyCharm, do this by selecting the red square on the tab at the bottom
    of PyCharm in the Run View entitled "app.py"
    ****
"""
# Step 3. Import the Flask request object (add it to the line below)
from flask import Flask, render_template, jsonify, Response
from schools import SchoolManager

app = Flask(__name__)
database = 'course_data.db'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/api/schools/<search_val>', methods=['GET'])
def get_schools(search_val: str) -> Response:
    # Step 4. Retrieve the 'column' and 'sort_by' values in the request.args dictionary sent
    #         from the client to the server.  (ex: request.args.get('key') )

    #         Pass them each into the find() method call below.  Restart your server and test it out!
    try:
        results = [str(school)
                   for school in SchoolManager(database).find(search_val)]
    except Exception as err:
        results = err.args

    return jsonify(schools=results, school_name=search_val)


app.run(host='localhost', port=8051)

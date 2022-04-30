# set the student_files folder on your PYTHONPATH

from flask import Flask, render_template, jsonify, Response
from ch07_frontend.flask_demo.capitals import capitals

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/state/<name>', methods=['GET'])
def get_capital(name='Colorado'):
    try:
        name_capitalized = ' '.join(word.capitalize() for word in name.split())
        resp = jsonify(state=name, capital=capitals[name_capitalized])
    except KeyError:
        resp = jsonify(state=name, capital='not found')

    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/state', methods=['GET'])
def list_states():
    resp = jsonify(names=[state for state in capitals], foo='bar')
    return Response(resp.data, status=200, mimetype='application/json')

app.run(host='localhost', port=8051)

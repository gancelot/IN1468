"""

    demo_app.py

"""

from flask import Flask, render_template, jsonify
from capitals import capitals

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/states/<name>', methods=['GET'])
def get_capital(name):
    try:
        name_capitalized = ' '.join(word.capitalize() for word in name.split())
        resp = jsonify(state=name, capital=capitals[name_capitalized])
    except KeyError:
        resp = jsonify(state=name, capital='not found')

    return resp


@app.route('/states', methods=['GET'])
def list_states():
    return jsonify(names=[state for state in capitals])


app.run(host='localhost', port=8051)

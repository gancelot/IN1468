import json
import logging
from pathlib import Path

from flask import redirect, Response, jsonify, request, current_app as app

from .genre import genre
from .schools import SchoolManager
from .simpsons import Simpsons

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()], format='%(levelname)s: %(message)s')

APP_ROOT = Path(__file__).parent
RESOURCES_DIR = APP_ROOT / 'resources'

logging.info(f'Using server root:{APP_ROOT}')
logging.info(f'Using resources directory:{RESOURCES_DIR}')


@app.route('/', methods=['GET'])
def index():
    """ Redirects localhost:8051 to localhost:8051/2020 causing main_page() to execute."""
    return redirect('/2020')


@app.route('/<year>', methods=['GET'])
def main_page(year='2020'):
    """
        Returns JSON data containing resolved top movies for a specified year (1990-2020)
        URL Syntax: localhost:8051/2015
    """
    filepath = RESOURCES_DIR / f'{year}.json'
    contents = {'err': 'Resource not found.'}
    try:
        with open(filepath, encoding='utf-8') as f:
            contents = f.read()
    except IOError:
        contents = json.dumps(contents)
    logging.info(f'Contents: {contents[:80]}...')
    return Response(contents, status=200, mimetype='application/json')


@app.route('/genre', methods=['GET'])
def list_genres():
    """
        Returns allowable genre values.
        URL Syntax: localhost:8051/genre
    """
    resp = jsonify(allowed_genre_values=list(genre.values()))
    logging.info(resp.data.decode())
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/genre/<id>', methods=['GET'])
def get_genre(id):
    """
        Returns JSON data containing resolved genre_id names
        URL Syntax: localhost:8051/genre/28
    """
    try:
        index = list(genre.values()).index(int(id))   # lookup genre
        genre_name = list(genre.keys())[index]
    except ValueError:
        genre_name = ''
    resp = jsonify(id=id, genre=genre_name)
    logging.info(resp.data.decode())
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/school', methods=['GET'])
def school_search():
    """
        Returns JSON data containing results from querying our school database from the last two chapters.
        Legal URL Syntax:
            localhost:8051/school?value=Loyola&column=fullname&sort_by=state
            localhost:8051/school?value=Loyola
            localhost:8051/school?value=A&column=state
            localhost:8051/school?value=ville&column=city&sort_by=state
    """
    # only pass params to the database that exist...(this way defaults in the function definition are used)
    params = ['value', 'column', 'sort_by']
    db_params = { param:request.args.get(param) for param in params if request.args.get(param) is not None}

    results, err = SchoolManager(APP_ROOT / 'course_data.db').find(**db_params)
    resp = jsonify(error_msg=err, **db_params, results=[str(result) for result in results])
    logging.info(resp.data.decode())
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/simpsons', methods=['GET'])
def get_simpsons():
    """
        Returns JSON data containing Simpsons character info
        URL Syntax: localhost:8051/simpsons?char_name=burns
    """
    name = request.args.get('char_name', None)
    results = Simpsons(APP_ROOT / 'course_data.db').find(name)
    logging.info(results)
    resp = jsonify(name=name, results=results)
    return Response(resp.data, status=200, mimetype='application/json')

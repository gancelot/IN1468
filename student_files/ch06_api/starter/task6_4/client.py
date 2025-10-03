"""
    ch06_api/starter/task6_4/client.py
    This task is the client component of our API client-server app.
    It makes requests, receives and processes a JSON response and
    renders it using PrettyTable.

    Sample URL request:
    http://localhost:8051/api/schools/ID?column=state&sort_by=city

    Instructions:
    Step 5. The client below is nearly the same as in the previous task (a couple of variable
            names were changed).  Also, the rendering of the data is changed (PrettyTable).
            Look over the client code below.
            Then, with your task6_4/app.py server running, run this file and verify the output.

"""
import click
import requests
from prettytable import PrettyTable


def make_request(url: str, params: dict = None) -> dict:
    resp = requests.get(url, params=params)

    print('Using: ', resp.url)
    print('\nThe Raw JSON response values:\n', resp.text)
    print('\nThe HTTP status:', resp.status_code)
    print('\nThe response headers:\n', resp.headers)

    return resp.json()


search_val = click.prompt('Enter a search value', default='Loyola')
url = f'http://localhost:8051/api/schools/{search_val}'

search_column = 'fullname'
sort_column = 'city'

results = make_request(url, params={'column': search_column, 'sort_by': sort_column})

print(f'\nResults for: {results.get("search_val")}')
schools = results.get('schools', [])

pt = None
if schools:
    pt = PrettyTable(schools[0].keys(), align='l')
    for school in schools:
        pt.add_row(school.values())
print(pt)

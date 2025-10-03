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


search_val = click.prompt('Enter a search value', default='ID')
url = f'http://localhost:8051/api/schools/{search_val}'

search_column = 'state'
sort_column = 'city'

results = make_request(url, params={'column': search_column, 'sort_by': sort_column})

print(f'\nResults for: {results.get("school_name")}')
schools = results.get('schools', [])

if schools:
    pt = PrettyTable(['School'])
    pt.align['School'] = 'l'
    for school in schools:
        pt.add_row([school])
    print(pt)

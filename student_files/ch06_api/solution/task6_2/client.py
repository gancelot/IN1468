import click
import requests
from prettytable import PrettyTable


def make_request(url: str) -> dict:
    resp = requests.get(url)

    print('Using: ', resp.url)
    print('\nThe Raw JSON response values:\n', resp.text)
    print('\nThe HTTP status:', resp.status_code)
    print('\nThe response headers:\n', resp.headers)

    return resp.json()


school_name = click.prompt('Enter a school name', default='Loyola')
url = f'http://localhost:8051/api/schools/{school_name}'

results = make_request(url)

print(f'\nResults for: {results.get("school_name")}')
schools = results.get('schools', [])

if schools:
    pt = PrettyTable(['School'])
    pt.align['School'] = 'l'
    for school in schools:
        pt.add_row([school])
    print(pt)

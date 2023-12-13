import click
import requests
from prettytable import PrettyTable

school_name = click.prompt('Enter a school name', default='Loyola')

url = f'http://localhost:8051/api/schools/{school_name}'

r = requests.get(url)
print('Using: ', r.url)

print('\nThe Raw JSON response values:\n', r.text)

results = r.json()
print(f'Results for: {results.get("school_name")}')
schools = results.get('results')
pt = PrettyTable(schools[0].keys())
for school in schools:
    pt.add_row(school.values())
print(pt)

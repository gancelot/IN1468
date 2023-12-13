import click
import requests

column = None
sort_by = None

school_name = click.prompt('Enter a school name', default='Loyola')

url = f'http://localhost:8051/school/{school_name}'

r = requests.get(url, params={'column': column, 'sort_by': sort_by})
print('Using: ', r.url)
print('Our client HTTP headers:\n', r.request.headers)
print('Flask server HTTP headers:\n', r.headers)
print('The Raw JSON response values:\n', r.text)
results = r.json()
print(f'Results for: {results.get("school_name")}')
for school in results.get('schools', []):
    print(school)

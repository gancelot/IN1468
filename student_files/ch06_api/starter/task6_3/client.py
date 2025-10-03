"""
   ch06_api/starter/task6_3/client.py -
   This is the client file developed in Task 6-2.
   You will add the ability to submit request parameters to the server.
"""
import click
import requests
from prettytable import PrettyTable


# Step 1. Add a params parameter (a dict) to this function.  It can have a default value of None.
#         This parameter will be used to modify the requests.get() call within the function to accept
#         the params parameter.
def make_request(url: str) -> dict:
    resp = requests.get(url)

    print('Using: ', resp.url)
    print('\nThe Raw JSON response values:\n', resp.text)
    print('\nThe HTTP status:', resp.status_code)
    print('\nThe response headers:\n', resp.headers)

    return resp.json()


search_val = click.prompt('Enter a search value', default='ID')
url = f'http://localhost:8051/api/schools/{search_val}'

search_column = 'state'
sort_column = 'city'

# Step 2. Modify the call to make_request() to accept a dictionary that has a 'column' key and
#         a 'sort_by' key.  Provide the two values above into this dictionary.  Pass the dictionary
#         into the params= parameter you created in step 1.
results = make_request(url)

print(f'\nResults for: {results.get("school_name")}')
schools = results.get('schools', [])

if schools:
    pt = PrettyTable(['School'])
    pt.align['School'] = 'l'
    for school in schools:
        pt.add_row([school])
    print(pt)

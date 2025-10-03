"""

	client.py - Works with the completed Task 6-1 server.

	1. Ensure the server from Task 6-1 is running.

"""
import click
import requests
from prettytable import PrettyTable


def make_request(url: str) -> dict:
    pass
    # 2. Remove the pass above.  Then,
    #       a) make a GET request to the above url (using requests), assign a Response object variable it

    #       b) print the url, text, status_code, and headers of the response object

    #       c) Return a dictionary of the response (hint: use resp.json())


school_name = click.prompt('Enter a school name', default='Loyola')
url = f'http://localhost:8051/api/schools/{school_name}'

# 3. Call the function above, pass the provided URL into it.  Be sure to capture the return value in a variable.

# 4. Obtain the returned matching school results.  This should be a list found within the
#    results under a key called 'schools'.  Use the dictionary get() method to obtain
#    the list of schools (strings):  results.get('schools').
#    Print them (optionally use PrettyTable to do this).

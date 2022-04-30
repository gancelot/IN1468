"""

    Example using urllib tools.
    To run this, first run ch08_network_apis/server/wsgi.py

"""
import sys
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

results = ''

query_str = {'value': 'foo', 'column': 'fullname', 'sort_by': 'state'}
url = 'http://localhost:8051/school?' + urlencode(query_str)
print(url)
try:
    with urlopen(url) as f:
        results = f.read().decode()
        print(f.status)
        print(f.reason)
        print(results)
except (URLError, UnicodeDecodeError) as err:
    print(f'Error: {err}', file=sys.stderr)

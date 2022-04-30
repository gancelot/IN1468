import sys

import requests
from bs4 import BeautifulSoup

payload = {
    'user_id': 'sample',
    'password': 'sample',
    'login': 'Login',
    'client_date_string': 'Thu Apr 07 2016 14:09:47 GMT-0600 (Mountain Standard Time)',
    'tz_offset': -6
}


with requests.Session() as session:
    try:
        req = session.post(url='https://foodclub.org/sample/login', data=payload)
        req2 = session.get('https://foodclub.org/sample/bookkeeper')
    except requests.RequestException:
        print('Error in request.')
        sys.exit()

    soup = BeautifulSoup(req2.text, 'html.parser')
    all_spans = soup.find_all('span')

    for one_span in all_spans:
        print(one_span.text)

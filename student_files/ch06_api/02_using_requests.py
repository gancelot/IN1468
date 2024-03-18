import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

# import mocklab        # only uncomment this if internet access is not available

print('Retrieving JSON using the requests library:')
feed = 'https://api.stackexchange.com/2.2/search?intitle=python&site=stackoverflow'
data_dict = requests.get(feed).json()
for idx, question in enumerate(data_dict.get('items', []), 1):
    print(idx, question.get('title'))
print('---')

#alternate way with params added on...
print('\nThe following uses params= to build the query string:')
feed = 'https://api.stackexchange.com/2.2/search'
query_str = {
    'intitle': 'python',
    'site': 'stackoverflow'
}
resp = requests.get(feed, params=query_str)
print(f'URL used: {resp.url}')


print('\nUsing basic authentication with requests:')
page = 'https://jigsaw.w3.org/HTTP/Basic/'
auth = HTTPBasicAuth('guest', 'guest')
page_text = requests.get(page, auth=auth).text

soup = BeautifulSoup(page_text, 'html.parser')
print(f'The page was parsed.  {soup.select('p')[2].text}')


page = requests.get('https://www.yahoo.com').text
soup = BeautifulSoup(page, 'html.parser')
print(soup.title.text)
print('\nObtaining H2 tags from yahoo.com:')
for tag in soup.find_all('h2'):
    print(tag.text)

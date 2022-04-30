import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


feed = 'https://api.stackexchange.com/2.2/search?intitle=python&site=stackoverflow'
data_dict = requests.get(feed).json()
for question in data_dict.get('items', []):
    print(question.get('title'))

#alternate way with params added on...
print('---')
print('Alternate way:')
feed = 'https://api.stackexchange.com/2.2/search'
query_str = {
    'intitle': 'python',
    'site': 'stackoverflow'
}
data_dict = requests.get(feed, params=query_str).json()
print([question.get('title') for question in data_dict.get('items', [])])


page = 'https://jigsaw.w3.org/HTTP/Basic/'
auth = HTTPBasicAuth('guest', 'guest')
page_text = requests.get(page, auth=auth).text
soup = BeautifulSoup(page_text, 'html.parser')
print(soup.select('p')[2].text)


page = requests.get('http://www.cisco.com').text
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)
print(soup.find_all('h2'))
p_tags = soup.find_all('p')
print(len(p_tags))
print(p_tags[2].text)
high_priority = soup.select('.pri-0')
if len(high_priority) > 0:
    print(high_priority[0].text)

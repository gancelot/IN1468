import requests
from threading import Thread


def load_data(url):
    data = None
    try:
        r = requests.get(url)
        data = r.json()
    except requests.exceptions.RequestException as err:
        print('Error retrieving data from {0}\nMessage: {1}'.format(url, err))

    return data


class DataFetcher(Thread):
    def __init__(self, url, name=''):
        super().__init__(name=name)
        self.url = url

    def run(self):
        print('Results: {0}'.format(load_data(self.url)))


if __name__ == '__main__':
    m = DataFetcher('https://inciweb.nwcg.gov/feeds/json/markers/', 'Worker')
    m.start()

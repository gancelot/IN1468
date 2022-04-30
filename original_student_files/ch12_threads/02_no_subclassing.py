from threading import Thread

import requests


def load_data(url):
    data = None
    try:
        r = requests.get(url)
        data = r.json()
        print(data)
    except requests.exceptions.RequestException as err:
        print('Error retrieving data from {0}\nMessage: {1}'.format(url, err))

    return data


if __name__ == '__main__':
    m = Thread(target=load_data, args=('https://inciweb.nwcg.gov/feeds/json/markers/',))
    m.start()

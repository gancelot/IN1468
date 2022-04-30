"""
    04_decorators.py

    Functions can exist within another function (closure)


"""
from urllib.request import urlopen


def set_url(url):
    def load():
        return urlopen(url).read()
    return load


get_google = set_url('http://www.google.com')
results = get_google()
print(results)

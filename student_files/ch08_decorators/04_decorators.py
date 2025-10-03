"""
    04_decorators.py

    Functions can exist within another function (closure)

    Note: Without internet, simply change the https://www.google.com URL to an internal
          URL and it should work.
"""
from urllib.request import urlopen


def set_url(url):
    def load():
        return urlopen(url).read()
    return load


get_google = set_url('http://www.google.com')
results = get_google()
print(results)

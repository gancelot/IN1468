"""

    05_static.py

    Note: Without internet, simply change the https://www.google.com URL to an internal
          URL and it should work.
"""
import urllib.request


class Page:
    @staticmethod
    def page_load(url):
        with urllib.request.urlopen(url) as f:
            results = f.read()

        return results


webpage = 'https://www.google.com'
print(Page.page_load(webpage))

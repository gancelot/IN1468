"""
    02_json_viewer.py
    A simple, recursive JSON viewer class.
    Accepts either a valid URL returning JSON data or a filepath containing JSON data
    Easy to use.
    See examples at the bottom.
"""
from json import loads
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import requests

class JSONViewer:
    def __init__(self, pathlike: Union[str, Path]):
        """pathlink can be a filepath with JSON contents or a url to process"""
        self.pathlike = pathlike
        self._depth = 0
        self._spacer = "  >  "

        if self._isurl():
            self._process_results(requests.get(self.pathlike).json())
        elif Path(pathlike).exists():
            results = Path(pathlike).read_text()
            self._process_results(loads(results))
        else:
            print('Invalid URL and/or file path')

    def _isurl(self) -> bool:
        """True if it is a valid URL, False otherwise, doesn't require third-party validators"""
        try:
            result = urlparse(self.pathlike)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def _process_results(self, results):
        self._depth += 4
        if isinstance(results, dict):
            for item in results:
                print(f'{" "*self._depth}{item}', end='')
                if isinstance(results[item], list) or isinstance(results[item], dict):
                    print()
                    self._process_results(results[item])
                else:
                    print(f'{self._spacer}{results[item]:<}')
        elif isinstance(results, list):
            for value in results:
                if isinstance(value, list) or isinstance(value, dict):
                    self._process_results(value)
                else:
                    print(f'{" "*self._depth}{value}')

        self._depth -= 4


if __name__ == '__main__':
    # from a network request, requires external network access
    JSONViewer('https://api.stackexchange.com/2.2/search?intitle=python&site=stackoverflow')

    # considered invalid URL by the class
    JSONViewer('api.stackexchange.com')

    # from a file
    JSONViewer('../resources/stackoverflow_data.json')

    # from a file
    JSONViewer(Path('../resources/json_file_save.json'))

    # from another file (invalid file)
    JSONViewer('foo.json')

    # from another URL (local), requires ch 8 server to be running
    JSONViewer('http://localhost:8051/school?value=Loyola')

    # from another URL (local), requires ch 8 server to be running
    JSONViewer('http://localhost:8051/simpsons?char_name=Homer')
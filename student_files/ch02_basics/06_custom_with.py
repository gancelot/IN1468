"""

    Making the with control work for you

"""
import sys
from ipaddress import ip_address

filename = '../resources/access_.log'


def acquire_data(filename, encoding='utf-8', sep=','):
    lines = []
    try:
        with open(filename, encoding=encoding) as f:
            for line in f:
                lines.append(line.strip().split(sep))
    except IOError as err:
        print(f'Error {err}', file=sys.stderr)

    return lines


results = acquire_data(filename, sep=' ')


class OutputRedirector:
    def __init__(self, filename, data, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.data = data

    def __enter__(self):
        self.file = open(self.filename, 'wt', encoding=self.encoding)
        self.stdout_prev = sys.stdout
        sys.stdout = self.file

    def __exit__(self, typ, val, tb):
        sys.stdout = self.stdout_prev
        if not self.file.closed:
            self.file.close()


with OutputRedirector('filtered_results.txt', results):
    for entry in results:
        try:
            print(ip_address(entry[0]))
        except ValueError:                                  # Raised when an ip_address() is not valid
            pass


# -----------------------------
# The above example can be accomplished using a built-in std library utility
# called redirect_stdout() as follows...
from contextlib import redirect_stdout
with redirect_stdout(open('filtered_results2.txt', 'wt', encoding='utf-8')):
    for entry in results:
        try:
            print(ip_address(entry[0]))
        except ValueError:
            pass

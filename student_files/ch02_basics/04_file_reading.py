"""

    Reading from Files

"""
import sys

f = None
lines = []
try:
    f = open('../resources/access_.log', encoding='utf-8')
    lines = f.readlines()
    print(len(lines), 'lines read.')
except IOError as err:
    print(err, file=sys.stderr)
finally:
    if f:
        f.close()

"""
    Reading a file 2 ways:
    - without using the with control
    - using the with control
"""
import os
import sys

path = '../resources'
filename = 'access_.log'
filepath = os.path.join(path, filename)

lines = []
f = None
try:
    f = open(filepath, encoding='utf-8')
    lines = f.readlines()
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)
finally:
    if f:
        f.close()

print(f'{len(lines)} lines read.')


# Using the with control
lines = []
try:
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
except IOError as err:
    print(f'Error {err}', file=sys.stderr)

print(f'{len(lines)} lines read.')

"""
    05_defaultdict.py
"""
from collections import defaultdict

d1 = defaultdict(str)
d1['greet1'] = 'hello'
print(d1['greet1'])     # works as expected
print(d1['greet2'])     # not valid, invokes the str() constructor as a result

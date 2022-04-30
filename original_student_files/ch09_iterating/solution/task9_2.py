"""

      task9_2.py   -   Using Generators and Dictionary Comprehensions

      This exercise is a refactoring of the task9_1.py solution.  It
      employs a generator to read data from a file.
"""
from collections import Counter
datafile = '../../resources/cities15000.txt'


def country_generator():
    with open(datafile, encoding='utf-8') as f:
        for line in f:
            yield line.split('\t')[8]


print(Counter(country_generator()).most_common(10))



# Side task...as a generator expression...
# (ugly, maybe, faster, probably, less memory, yes)

print(Counter((line.split('\t')[8] for line in open(datafile, encoding='utf-8'))).most_common(10))

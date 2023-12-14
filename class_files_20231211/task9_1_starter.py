"""

      task9_1_starter.py   -   Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.


"""
from collections import Counter

datafile = '../resources/cities15000.txt'

countries = []

with open(datafile, encoding='utf-8') as f:
    for line in f:
        countries.append(line.split('\t')[8])

print(Counter(countries).most_common(10))

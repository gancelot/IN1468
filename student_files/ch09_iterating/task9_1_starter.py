"""

      task9_1_starter.py   -   Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.


"""
from argparse import ArgumentParser
from collections import Counter

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-c', '--count', default=3, type=int)
    return parser.parse_args()


count = get_args().count

datafile = '../resources/cities15000.txt'
countries = []

with open(datafile, encoding='utf-8') as f:
    for line in f:
        countries.append(line.split('\t')[8])

print(Counter(countries).most_common(count))


# ============================================
# Generator version...
def countries_generator():
    with open(datafile, encoding='utf-8') as f:
        for line in f:
            yield line.split('\t')[8]


print(Counter(countries_generator()).most_common(count))


# ===================================
# Generator expression version.
c = Counter( (line.split('\t')[8] for line in open(datafile, encoding='utf-8')) )
print(c.most_common(count))
print(len(c))

"""

      task9_3.py   -   Using the argparse Module

      This exercise is a refactoring of the task9_1.py solution.  It
      proposes using a generator to read data from a file
      and a dictionary comprehension to build the country_names dictionary.
"""
import argparse
from collections import Counter

datafile = '../../resources/cities15000.txt'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default='3', type=int, help='The number of countries to retrieve')
    return parser.parse_args()


def country_generator(filename):
    with open(filename, encoding='utf8') as cities_file:
        for line in cities_file:
            yield line.strip().split('\t')[8]

most_common = Counter(country_generator(datafile)).most_common(get_args().count)
print(most_common)

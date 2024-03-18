"""

      task3_3.py   -   Using the argparse Module

      This exercise is a refactoring of the task3_2.py solution.  It
      uses argparse to read from the command line how many top countries
      are desired.
"""
import argparse
from collections import Counter
from typing import Generator

datafile = '../../resources/cities15000.txt'


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default='3', type=int, help='The number of countries to retrieve')
    return parser.parse_args()


def country_generator(filename) -> Generator[str, None, None]:
    with open(filename, encoding='utf-8') as cities_file:
        for line in cities_file:
            yield line.strip().split('\t')[8]


most_common = Counter(country_generator(datafile)).most_common(get_args().count)
print(most_common)

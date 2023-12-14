"""

      task9_3_starter.py   -   Using the argparse Module

      This exercise is a refactoring of the task9_2.py solution.  It
      proposes parsing command-line arguments to determine how many results to display.
      The following command line arguments shall be used:

        python task9_3_starter.py -c 5

		    or

        python task9_3_starter.py --count 5

"""
import argparse
from collections import Counter

datafile = '../resources/cities15000.txt'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default=3, type=int)
    return parser.parse_args()


args = get_args()


def get_countries():
    with open(datafile, encoding='utf-8') as f:
        for line in f:
            yield line.split('\t')[8]


print(Counter(get_countries()).most_common(args.count))


# Generator expression version:
print(Counter((line.split('\t')[8] for line in open(datafile, encoding='utf-8'))).most_common(args.count))

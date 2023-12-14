"""

      task9_2_starter.py   -   Using Generators and Dictionary Comprehensions

       Working from your previous solution for task6_1_starter.py, or by using
       the solution below, modify this solution to use a generator.



"""
from collections import Counter

datafile = '../resources/cities15000.txt'


def get_countries():
    with open(datafile, encoding='utf-8') as f:
        for line in f:
            yield line.split('\t')[8]


print(Counter(get_countries()).most_common(10))


# Generator expression version:
print(Counter((line.split('\t')[8] for line in open(datafile, encoding='utf-8'))).most_common(10))

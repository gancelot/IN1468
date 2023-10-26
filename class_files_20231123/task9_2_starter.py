import argparse
from collections import Counter

datafile = '../resources/cities15000.txt'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default=3, type=int)
    return parser.parse_args()

args = get_args()

def country_count_generator():
    with open(datafile, encoding='utf-8') as f:
        for line in f:
            yield line.split('\t')[8]

print(Counter(country_count_generator()).most_common(args.count))
print(Counter((line.split('\t')[8] for line in open(datafile, encoding='utf-8'))).most_common(args.count))

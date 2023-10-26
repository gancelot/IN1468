from collections import Counter

datafile = '../resources/cities15000.txt'

countries = []

with open(datafile, encoding='utf-8') as f:
    for line in f:
        country = line.split('\t')[8]
        countries.append(country)

print(Counter(countries).most_common(10))

"""

    Sorting techniques.

"""
sa_countries = [
    ('Brazil', 216_000_000),
    ('Peru', 34_300_000),
    ('Columbia', 52_000_000),
    ('Argentina', 45_700_000)
]


def sort_by_population(country):
    return country[1]


def sort_by_name(country):
    return country[0]


sa_countries.sort(key=sort_by_population)
print(sa_countries)


new_ctys = sorted(sa_countries, key=sort_by_name, reverse=True)
print(new_ctys)


print('\nsorting records using a key and lambda:')
sa_countries.sort(key=lambda country: country[1], reverse=True)
print(sa_countries)

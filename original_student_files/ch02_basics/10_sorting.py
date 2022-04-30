"""

    Sorting techniques.

"""
sa_countries = [
    ('Brazil', 204000000), ('Columbia', 48500000),
    ('Argentina', 43100000), ('Peru', 31100000)
]

# in-place sort
sa_countries.sort()
print(sa_countries)


# creating a new list by sorting
new_countries = sorted(sa_countries)
print(new_countries)


# sorting in reverse (both in-place and returning a new list)
sa_countries.sort(reverse=True)
new_countries = sorted(sa_countries, reverse=True)
print(sa_countries)
print(new_countries)

# getting a reverse-iterator
for i in reversed(range(10)):
    print(i, end=' ')
else:
    print()


# sort() using a key
def sort_by_population(country):
    return country[1]


sa_countries.sort(key=sort_by_population)
print(sa_countries)


# sorted() using a key
new_countries = sorted(sa_countries, key=sort_by_population, reverse=True)
print(new_countries)


# sorting records using a key and lambda
sa_countries.sort(key=lambda country: country[1], reverse=True)
print(sa_countries)

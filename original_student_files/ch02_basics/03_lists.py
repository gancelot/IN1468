sa_countries = [
    ('Brazil', 204_000_000), ('Columbia', 48_500_000),
    ('Argentina', 43_100_000), ('Peru', 31_100_000),
    ('Venezuela', 30_600_000), ('Chile', 18_000_000),
    ('Equador', 16_300_000), ('Bolivia', 10_500_000),
    ('Paraguay', 7_000_000), ('Uruguay', 3_300_000),
    ('Guyana', 747_000), ('Suriname', 560_000),
    ('French Guiana', 262_000)
]

# Showing how lists support slicing, random access, and membership
print(sa_countries[2])
print(sa_countries[-2:])
print('brazil'.capitalize() in [country for country, pop in sa_countries])

# to check if something is a Sequence:
from collections.abc import Sequence
print(f'sa_countries is a Sequence: {isinstance(sa_countries, Sequence)}')


sa_countries = [
    ('Brazil', 204_000_000), ('Columbia', 48_500_000),
    ('Argentina', 43_100_000), ('Peru', 31_100_000),
 ]

sa_countries.append(('Falkland Islands', 3000))
sa_countries.insert(1, ('Chile', 18_000_000))
print(sa_countries)

print(max(sa_countries, key=lambda country: country[1]))

for country, pop in sa_countries:
    print(country)

"""
    Demonstration of namedtuples.
"""
from collections import namedtuple

Country = namedtuple('CountryRecord', 'name population')

sa_countries = [
    Country('Brazil', 204000000), Country('Columbia', 48500000),
    Country('Argentina', 43100000), Country('Peru', 31100000),
    Country('Venezuela', 30600000), Country('Chile', 18000000),
    Country('Equador', 16300000), Country('Bolivia', 10500000),
    Country('Paraguay', 7000000), Country('Uruguay', 3300000),
    Country('Guyana', 747000), Country('Suriname', 560000),
    Country('French Guiana', 262000), Country('Falkland Islands', 3000)
]

sa_countries.sort(key=lambda country: country.name)

for record in sa_countries:
    print(f'{record.name:<20}{record.population:>15}')

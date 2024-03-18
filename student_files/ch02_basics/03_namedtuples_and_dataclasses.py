"""

    namedtuples, typed NamedTuples, and dataclasses

"""
from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple

# classic namedtuple
Country = namedtuple('Country', 'name population')

# typed NamedTuple
Country = NamedTuple('Country', [('name', str), ('population', int)])


# or alternatively...
class Country(NamedTuple):
    name: str
    population: int = 0


# dataclass
@dataclass
class Country:
    name: str
    population: int = 0


sa_countries = [
    Country('Brazil', 216_000_000), Country('Columbia', 52_000_000),
    Country('Argentina', 45_700_000), Country('Peru', 34_300_000),
    Country('Venezuela', 28_800_000), Country('Chile', 19_600_000),
    Country('Ecuador', 18_200_000), Country('Bolivia', 12_400_000),
    Country('Paraguay', 6_800_000), Country('Uruguay', 3_400_000),
    Country('Guyana', 813_000), Country('Suriname', 623_000),
    Country('French Guiana', 312_000), Country('Falkland Islands', 3_800)
]

sa_countries.sort(key=lambda country: country.name)

for ctry in sa_countries:
    print(f'{ctry.name:<20}{ctry.population:>15,}')

"""

    List comprehensions.

"""
from pathlib import Path

sa_countries = [
    ('Brazil', 216_000_000), ('Columbia', 52_000_000),
    ('Argentina', 45_700_000), ('Peru', 34_300_000),
    ('Venezuela', 28_800_000), ('Chile', 19_600_000),
    ('Ecuador', 18_200_000), ('Bolivia', 12_400_000),
    ('Paraguay', 6_800_000), ('Uruguay', 3_400_000),
    ('Guyana', 813_000), ('Suriname', 623_000),
    ('French Guiana', 312_000), ('Falkland Islands', 3_800)
]

# using a list comprehension to get countries with populations over 20 million
larger = [country for country, pop in sa_countries if pop >= 20_000_000]
print(larger)


city_names = []
filepath = Path('../resources/cities15000.txt')
if filepath.exists():
    city_names = [line.split('\t')[1] for line in filepath.open(encoding='utf-8')]
print(city_names)

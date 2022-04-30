"""

    List comprehensions.

"""
from pathlib import Path

sa_countries = [
    ('Brazil', 204000000), ('Columbia', 48500000),
    ('Argentina', 43100000), ('Peru', 31100000),
    ('Venezuela', 30600000), ('Chile', 18000000),
    ('Equador', 16300000), ('Bolivia', 10500000),
    ('Paraguay', 7000000), ('Uruguay', 3300000),
    ('Guyana', 747000), ('Suriname', 560000),
    ('French Guiana', 262000),
]

# using a list comprehension to get countries with populations over 20 million
# uses a feature of Python 3.6
larger = [country for country, pop in sa_countries if pop >= 20_000_000]
print(larger)


city_names = []
filepath = Path('../resources/cities15000.txt')
if filepath.exists():
    city_names = [line.split('\t')[1] for line in filepath.open(encoding='utf-8')]
print(city_names)

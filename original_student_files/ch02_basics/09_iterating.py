"""

    Iterating techniques.

"""
from pathlib import Path
filepath = Path('../resources/sa_countries.csv')
sa_countries = []
with filepath.open(encoding='utf-8') as f:
    for line in f:
        sa_countries.append(line.strip().split(','))

print(sa_countries)

for value in enumerate(reversed(sa_countries[0])):
    print(value)

for country, pop in zip(*sa_countries):
    print(f'{country:<20}{pop:>15}')

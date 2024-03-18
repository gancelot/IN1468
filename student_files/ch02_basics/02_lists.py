"""

    Working with Sequences

"""
sa_countries = [
    ('Brazil', 216_000_000), ('Columbia', 52_000_000),
    ('Argentina', 45_700_000), ('Peru', 34_300_000),
    ('Venezuela', 28_800_000), ('Chile', 19_600_000),
    ('Ecuador', 18_200_000), ('Bolivia', 12_400_000),
    ('Paraguay', 6_800_000), ('Uruguay', 3_400_000),
    ('Guyana', 813_000), ('Suriname', 623_000),
    ('French Guiana', 312_000), ('Falkland Islands', 3_800)
]

# Showing how lists support slicing, random access, and membership
print(sa_countries[2])
print(sa_countries[-2:])
print('brazil'.capitalize() in [country for country, pop in sa_countries])

# to check if something is a Sequence:
from collections.abc import Sequence
print(f'sa_countries is a Sequence: {isinstance(sa_countries, Sequence)}')

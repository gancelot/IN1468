"""

    Sets.

"""
sa_countries = [
    ('Brazil', 204000000), ('Columbia', 48500000),
    ('Argentina', 43100000), ('Peru', 31100000),
    ('Venezuela', 30600000), ('Chile', 18000000),
    ('Equador', 16300000), ('Bolivia', 10500000),
    ('Paraguay', 7000000), ('Uruguay', 3300000),
    ('Guyana', 747000), ('Suriname', 560000),
    ('French Guiana', 262000),
]

countries_set = set(sa_countries)

print(len(countries_set))                       # 13
countries_set.add(('Brazil', 204000000))
print(len(countries_set))                       # 13
countries_set.add(('Brazil', 1))
print(len(countries_set))                       # 14


"""

    Dictionaries--new and old.

"""

# Creating a dict
country = {'name': 'Brazil', 'population': 204000000}


# Accessing a dict (safely)
print(country.get('name'))                  # returns Brazil
print(country.get('capital', 'N/A'))        # returns N/A


# Handling dict access when using [] notation
try:
    capital = country['capital']            # generates a KeyError
except KeyError:
    capital = '(unknown)'


# Adding entries to a dict
country['capital'] = 'Brasilia'


# Iterating a dict (gives keys back)
for key in country:
    print(f'{key}: {country[key]}', end=' ')
else:
    print()


# Getting just the values back from a dict
for value in country.values():
    print(value, end=' ')
else:
    print()


# Get both key and value back at the same time
for key, val in country.items():
    print(f'Key: {key}, Value: {val}', end=' ')
print()

countries = {
    'Brazil': {'population': 204000000, 'capital': 'Brasilia'},
    'Argentina': {'population': 43100000, 'capital': 'Buenos Aires'},
    'Venezuela': {'population': 30600000, 'capital': 'Caracas'}
}

countries_sorted = [(country_name, country.get('capital', 'N/A')) for country_name, country in sorted(countries.items())]
print(countries_sorted)


# -------------------------------------------------------------
# using an OrderedDict (Python 3.5 and earlier as dicts are now ordered by default)
from collections import OrderedDict

od = OrderedDict([('Smith', 43), ('James', 32), ('Edwards', 36), ('Cramer', 29)])
for key in od:
    print(key)

od.move_to_end('Smith')
for key in od:
    print(key)


# --------------------------------------------------------------
# using a defaultdict
from collections import defaultdict
dict1 = defaultdict(str)
dict1['greet1'] = 'hello'
print(dict1['greet1'], dict1['greet2'])

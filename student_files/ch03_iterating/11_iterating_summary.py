"""

    11_iterating_summary.py

"""
# numerous ways to iterate in Python....
for item in enumerate([5, 8, 9], 10):
    print(item[0], item[1])

for item in enumerate([5, 8, 9], 10):
    print('({}, {})'.format(*item))

for (count, value) in enumerate([5, 8, 9], 10):
    print(count, value)

for count, value in enumerate([5, 8, 9], 10):
    print(count, value)

for item in reversed([5, 8, 9]):
    print(item)

for item in enumerate(reversed([5, 8, 9])):
    print(item)

array1 = ['a', 'b', 'c']
array2 = [30, 40, 50]

for item1, item2 in zip(array1, array2):
    print(item1, item2)

from itertools import chain
for item in chain(array1, array2):
    print(item, end=' ')

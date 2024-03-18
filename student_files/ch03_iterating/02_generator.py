"""

    02_generator.py

"""


def a_generator(min_val, max_val):
    current_val = min_val
    while current_val <= max_val:
        yield current_val
        current_val += 1


gen = a_generator(3, 5)
print(type(gen))

# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for val in gen:
    print(val)

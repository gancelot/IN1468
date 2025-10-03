"""
    06_counter.py
"""
from collections import Counter

items = [1, 2, 3, 4, 5, 4, 4, 3, 4, 5, 2, 0, 7, 4, 5, 6]

top_most = Counter(items).most_common(1)             # 1 defines how many of the "mosts" to return
print(top_most)                                      # each "most" is a tuple of two values: most, num_occurrences


top_two_most = Counter(items).most_common(2)            # [(4, 5), (5, 3)]
print(top_two_most)

top_three_most = Counter(items).most_common(3)          # [(4, 5), (5, 3), (2, 2)]
print(top_three_most)

"""

      task9_2_starter.py   -   Using Generators and Dictionary Comprehensions

       Working from your previous solution for task6_1_starter.py, or by using
       the solution below, modify this solution to use a generator.



"""
from collections import Counter

datafile = '../resources/cities15000.txt'
cities = []


# Step 1. Modify this code to work within a generator.  Yield back one country
#         code value at a time.
with open(datafile, encoding='utf8') as cities_file:
    for line in cities_file:
        cities.append(line.strip().split('\t')[8])

# Step 2. Modify this code to invoke the generator within the Counter() constructor.
most_common = Counter(cities).most_common(10)
print(most_common)



# Step 3. Test it to get it working.  Refactor it as a generator expression.


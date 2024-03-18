"""

      task3_1.py   -           Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.


"""
from collections import Counter

datafile = '../../resources/cities15000.txt'

# Step 1. Create a sequence to hold country data read from the file
countries = []

# Step 2. Read country data (column 8) from the datafile above.  Store the
#         results in a list.
with open(datafile, encoding='utf-8') as f:
    for line in f:
        country = line.split('\t')[8]
        countries.append(country)

# Step 3. Using the Counter class, determine the top countries with the most cities with
#         populations over 15000.  Display your results.
print(Counter(countries).most_common(10))


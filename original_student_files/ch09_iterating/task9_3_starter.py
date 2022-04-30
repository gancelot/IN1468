"""

      task9_3_starter.py   -   Using the argparse Module

      This exercise is a refactoring of the task9_2.py solution.  It
      proposes parsing command-line arguments to determine how many results to display.
      The following command line arguments shall be used:

        python task9_3_starter.py -c 5

		    or

        python task9_3_starter.py --count 5

"""
from collections import Counter

datafile = '../resources/cities15000.txt'


# Step 1. Create a function called get_args() that instantiates the argument parser
#         from the argparse module.  Have it detect the -c argument value.  get_args()
#         should return an appropriate item to use in the most_common() call below.

def country_generator(filename):
    with open(filename, encoding='utf8') as cities_file:
        for line in cities_file:
            yield line.strip().split('\t')[8]

# Step 2. Replace the hardcoded value within the most_common() call below with the
#         result from parsing command-line arguments.
most_common = Counter(country_generator(datafile)).most_common(5)
print(most_common)

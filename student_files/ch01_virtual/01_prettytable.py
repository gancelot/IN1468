"""
    01_prettytable.py

    Demonstration of Virtual Environments
    The prettytable tool will not exist within the newly created
    virtual environment.  It will need to be installed by the pip
    tool within the virtual environment.

"""
from prettytable import PrettyTable, from_csv

# example 1, simple example
p = PrettyTable(['Win', 'Place', 'Show'])
p.add_row(['Homer', 'Bart', 'Lisa'])
print(p)

# example 2, data loaded from a csv
with open('../resources/simpsons.csv') as f:
    chars = from_csv(f)
    for col in ('Actor', 'Role', 'Episode_Debut'):
        chars.align[col] = 'l'
print(chars)

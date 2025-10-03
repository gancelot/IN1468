import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

contacts = pd.read_csv('contacts.dat', header=None, dtype='str')
contacts.columns = ['name', 'address', 'state', 'zip', 'area_code', 'phone', 'email', 'company', 'position']

print(contacts)

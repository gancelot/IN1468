"""
        16_boolean_indexing.py
"""
import pandas as pd

sat_temps = pd.DataFrame(data=[(78, 50), (82, 52), (83, 53)],
                         index=['Colorado Springs', 'Canon City', 'Pueblo'],
                         columns=['High', 'Low'])
print(sat_temps)
# Find any records where BOTH high and low temps are above 51 degrees
print(sat_temps.loc[(sat_temps['High'] >= 51) & (sat_temps['Low'] >= 51)])

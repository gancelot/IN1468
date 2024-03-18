"""

      03_masking - Use of Boolean Indexing expressions

"""
import numpy as np

print('\nBoolean Indexing (masking):')
arr15 = np.arange(1, 7)                                 # [1 2 3 4 5 6]
mask = arr15 <= 3                                       # arr <= 3 yields: [True, True, True, False, False, False]
print(arr15[mask])                                      # [1 2 3]

print('\nConsidering the following array:')
arr16 = np.arange(11, 29, 2).reshape(3, 3)              # [[11 13 15]
                                                        #  [17 19 21]
                                                        #  [23 25 27]]
print(arr16)

print('\nSelecting columns:')
mask = arr16[0] > 12
print(arr16[:, mask])                                   # [[13 15]
                                                        #  [19 21]
                                                        #  [25 27]]

print('\nSelecting Rows (based on a criterion):')
mask = arr16[:, 2] > 15
print(arr16[mask])                                      # [[17 19 21]
                                                        #  [23 25 27]]

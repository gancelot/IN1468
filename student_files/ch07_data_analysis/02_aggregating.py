"""

      02_aggregating - functions that aggregate results based on the items selected

"""
import numpy as np

arr7 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])


print(np.sum(arr7))                                                # 78
print(arr7.sum())                                                  # 78

print(np.mean(arr7[:, 0]))                                         # 5.5
print(arr7[:, 0].mean())                                           # 5.5

print(np.prod(arr7[:2, :2]))                                       # 40
print(arr7[:2, :2].prod())                                         # 40
print(arr7.prod(axis=1))                                           # [   6  120  504 1320]

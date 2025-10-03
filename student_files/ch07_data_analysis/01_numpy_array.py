"""
      01_numpy_array - the following illustrates different ways to create
                       numpy arrays and their attributes
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print('arr:\n', arr)
print(type(arr))                # <class 'numpy.ndarray'>

arr2 = np.array([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10]
])

arr3 = np.array([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]
])

print('\narr3:\n', arr3)
print(f'Shape: {arr3.shape}')
print(f'Size: {arr3.size}')
print(f'Axes: {arr3.ndim}')
print(f'dtype: {arr3.dtype}')

print(arr3)                     # [[ 1  2  3][4  5  6][7  8  9][10 11 12]]
print(arr3[0])                  # [1 2 3]
print(arr3[0][2])               # 3

arr5 = np.array([[1, 2, 3],
                 [4, 5., 6],
                 [7, 8, 9],
                 [10, 11, 12]])
print('\narr5:\n', arr5)
print('dtype of arr5:', arr5.dtype)

arr6 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])
print('arr6:\n', arr6)
print('Second column: ', arr6[:, 1])
print('Third row: ', arr6[2, :])

print('\narr6 reshaped:\n', arr6.reshape((2, 6)))

arr8 = np.zeros((2, 2))
print('arr8:\n', arr8)                     # [[ 0. 0.] [ 0. 0.]]

arr9 = np.ones((2, 2))
print('arr9:\n', arr9)                     # [[ 1. 1.] [ 1. 1.]]

arr10 = np.full((2, 2), 6)
print('arr10:\n', arr10)                    # [[ 6. 6.] [ 6. 6.]]

# linspace(start, end, num) - creates an array with num number of items evenly spaced between start and end
arr12 = np.linspace(0, 20, 5)       # [ 0. 5. 10. 15. 20. ]
print('arr12:\n', arr12)

arr13 = np.arange(0, 15, 3)         # [ 0 3 6 9 12 ]
print('arr13:\n', arr13)

np.random.seed(1001)
arr14 = np.random.rand(2, 3)        # [[ 0.30623218  0.26506357  0.19606006] [0.43052148  0.02311355  0.19578192]]
print(arr14)

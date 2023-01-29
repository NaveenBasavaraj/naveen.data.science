# Introduction to Numpy

import numpy as np

## Datatypes and Attributes

### numpys main datatype is ndarray

a1 = np.array([1, 2, 3])

print(a1)  # [1,2,3]
print(type(a1))  # <class 'numpy.ndarray'>
print(a1.shape)  # (3,)
print(a1.ndim)  # 1
print(a1.dtype)  # int64

a2 = np.array([[1, 2.0, 3], [7.7, 8, 9.3]])

print(a2)
'''
[[1.  2.  3. ]
 [7.7 8.  9.3]]
'''
print(type(a2))  # <class 'numpy.ndarray'>
print(a2.shape)  # (2, 3)
print(a2.ndim)  #1
print(a2.dtype)  # float64

a3 = np.array([[[1, 2.0, 3], [7.7, 8, 9.3]], [[3, 2.0, 3], [5.7, 8, 9.3]]])

print(a3)
'''
 [[3.  2.  3. ]
  [5.7 8.  9.3]]]
'''
print(type(a3))  # <class 'numpy.ndarray'>
print(a3.shape)  # (2, 2, 3)
print(a3.ndim)  # 3
print(a3.dtype)  # float64

# size gives us total elements
print(a1.size, a2.size, a3.size)  #3 6 12

# creating a dataframe using numpy array

a4 = [[9.9, 1.1, 2.2], [3.3, 4.4, 5.5]]
a4 = np.array(a4)

import pandas as pd

df = pd.DataFrame(a4)

print(df)

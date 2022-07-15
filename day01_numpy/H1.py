import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

b = np.array([1,2,3,4,5], ndmin=3)
print(b)
print(b.shape)
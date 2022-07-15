import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[2:6])
print(a[6:])
print(a[:5])
print(a[-5:-1])
print(a[:9:3])

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b[0,1:3])
print(b[0:2, 1])
print(b[0:2, 1:3])
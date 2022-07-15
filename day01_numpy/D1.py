import numpy as np

a = np.array([1,2,3,4,5])
print(a[2] + a[4])
print()

b = np.array([[1,2,3],[4,5,6]])
#print(b)
print(b[1,-3])
print(b[0,2])

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(c[1,1,0])
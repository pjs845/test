import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.shape)

a2 = a.reshape(4,3)
print(a2)
print(a2.shape)

a3 = a.reshape(2,3,2)
print(a3)
print(a3.shape)
print(a3.base)
print()

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b2 = b.reshape(-1)
print(b2)
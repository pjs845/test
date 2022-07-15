import numpy as np

a = np.array([1,2])
b = np.array([3,4])

c1 = np.concatenate((a,b))
print(c1)
c2 = np.stack((a,b))
print(c2)
print()

c3 = np.hstack((a,b))
print(c3)
c4 = np.vstack((a,b))
print(c4)
print()
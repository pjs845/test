import numpy as np

a = np.array([1,2,3,4,5])
a2 = a.copy()
a3 = a.view()
a[0] = 10
print(a)
print(a2)
print(a3)
print()

print(a2.base)
print(a3.base)
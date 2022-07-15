import numpy as np
a = np.array([1,2,3,4,5])
print(a.dtype)

b = np.array(["tiger", "lion", "rabbit"])
print(b.dtype)

c = np.array([1,2,3,4,5], dtype='S')
print(c.dtype)

d = np.array([1,2,3,4,5], dtype='i8')
print(d)
print(d.dtype)

e = np.array([1.3, 2.5, 3.8])
e2 = e.astype('i')
e2 = e.astype(int)
print(e2)
print(e2.dtype)

f = np.array([-2, 0, 1, 5])
f2 = f.astype(bool)
print(f2)
print(f2.dtype)
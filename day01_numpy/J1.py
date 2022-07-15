import numpy as np

a = np.array([1,2,3,4,5]) #1차원
for x in a:
    print(x)
print()

b = np.array([[1,2],[3,4]])
for x in b:
    for y in x:
        print(y)
print()

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])#3차원
for x in c:
    for y in x:
        for z in y:
            print(z)
print()

for x in np.nditer(c):
    print(x)
print()

d = np.array([1,2,3,4,5])
for i, x in np.ndenumerate(d):
    print(i,x)
print()

e = np.array([[1,2],[3,4]])
for i,x in np.ndenumerate(e):
    print(i,x)
print()
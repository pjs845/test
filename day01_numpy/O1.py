from numpy import random as r

x = r.randint(100) #0 ~(n-1)
print(x)

x2 = r.rand()
print(x2)

x3 = r.randint(100, size=(5))
print(x3)
print()

x4 = r.randint(100, size=(3,5))
print(x4)

x5 = r.rand(5)
print(x5)

x6 = r.rand(3,5)
print(x6)

x7 = r.choice([1,2,3,4])
print(x7)

x8 = r.choice([1,2,3,4], size=(3,4))
print(x8)
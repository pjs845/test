import matplotlib.pyplot as plt
from numpy import random as r

#x = r.normal(size=(2,3))
#x = r.normal(size=100)
x = r.normal(100, 10, 500)
print(x)

plt.hist(x)
plt.show()
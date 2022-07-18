# 다항 회귀(Polynomial Regression) : Bad Fit
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]

a = np.polyfit(x, y, 3)
mymodel = np.poly1d(a)

myline = np.linspace(2, 90, 200)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

r = r2_score(y, mymodel(x))
print("r", r)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [2,3,4,6,7,8,9,10,11,13,14,15,16,17,19,20,22,23]
y = [101,91,81,61,61,56,61,66,71,71,76,77,79,80,91,100,100,101]

a = np.polyfit(x, y, 3)
mymodel = np.poly1d(a)
myline = np.linspace(2, 23, 200)

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(y, mymodel(x))
print("r2", r2)

predict = mymodel(18)
print("predict", predict)
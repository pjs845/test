import matplotlib.pyplot as plt
import numpy as np

xp = np.array(["A", "B", "C", "D"])
yp = np.array([20, 80, 50, 70])

#plt.bar(xp, yp)
#plt.bar(xp, yp, color='green', width=0.3)
#plt.barh(xp, yp)
plt.barh(xp, yp, color='red', height=0.5)

plt.show()
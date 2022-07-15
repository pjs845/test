import matplotlib.pyplot as plt
import numpy as np

yp1 = np.array([2, 8, 1, 9, 5, 7])
plt.subplot(1,2,1)
#plt.subplot(2,1,1)
plt.plot(yp1)
plt.title("Title1")

yp2 = np.array([1, 9, 2, 8, 3, 5])
plt.subplot(1,2,2) 
#plt.subplot(2,1,2)
plt.plot(yp2)
plt.title("Title2")

plt.suptitle("Top Title")
plt.show()
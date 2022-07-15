import matplotlib.pyplot as plt
import numpy as np

yp = np.array([2, 8, 1, 9, 5, 7])

#plt.plot(yp, linestyle="dotted")
#plt.plot(yp, ls=":")

#plt.plot(yp, linestyle="dashed")
#plt.plot(yp, ls="--")

#plt.plot(yp, ls="-")
#plt.plot(yp, ls="-.")


#plt.plot(yp, color='r')
#plt.plot(yp, color='#34a1eb')

#plt.plot(yp, color='r', linewidth='15')

yp2 = np.array([4, 7, 2, 8, 6, 3])
plt.plot(yp)
plt.plot(yp2)
plt.show()
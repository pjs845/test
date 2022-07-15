import matplotlib.pyplot as plt
import numpy as np

yp = np.array([2, 8, 1, 9, 5, 7])
#plt.plot(yp, marker='o')
#plt.plot(yp, marker='*')
#plt.plot(yp, marker='D')
#plt.plot(yp, 'o:r')
#plt.plot(yp, 'o:g')
#plt.plot(yp, 'o-.')
#plt.plot(yp, 'o-.', ms=25)
#plt.plot(yp, 'o-.', ms=25, mec='r', mfc='y')
plt.plot(yp, 'o-.', ms=25, mec='#34ebb1', mfc='#34a1eb')
plt.show()

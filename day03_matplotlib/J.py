import matplotlib.pyplot as plt
import numpy as np

yp = np.array([30, 20, 40, 10])
parklabels = ["tiger", "rabbit", "lion", "mouse"]
parkexplode = [0.3, 0, 0.1, 0]
parkcolors = ["red", "green", "blue", "yellow"]
#plt.pie(yp, labels=parklabels) #각의 기준 : x축 right / counterclockwise(반시계방향)
#plt.pie(yp, labels=parklabels, startangle=90) 
plt.pie(yp, labels=parklabels, explode=parkexplode, colors=parkcolors)
#plt.legend()
plt.legend(title="Animals")
plt.show()
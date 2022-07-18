import numpy as np
import matplotlib.pyplot as plt

#빅데이터 분포
x = np.random.uniform(0.0, 5.0, 1000000)
print(x)

plt.hist(x)
plt.show()
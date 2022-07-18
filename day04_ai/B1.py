import numpy as np

a = [6,32,44,49,51,42,8,12,16,40,81,83,33,3,9,7,26,37,28,62,32]

#75%가 44이하
x = np.percentile(a, 75)
print(x)

x = np.percentile(a, 85)
print(x)
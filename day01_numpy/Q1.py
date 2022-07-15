from numpy import random as r
import numpy as np

a = [1,2,3,4,5]
x = np.array(a)
print(x)
y = r.permutation(x) # 혼합 : 원본배열 바꾸지않고, 변경
print(x)
print(y)
print()

r.shuffle(x)
print(x)
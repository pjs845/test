# 선형 회귀 (Linear Regression) : Good Fit
import matplotlib.pyplot as plt
from scipy import stats

x = [6,8,9,8,3,18,3,10,5,12,13,10,7]
y = [100,87,88,89,112,87,104,88,95,79,78,86,87]

#plt.scatter(x,y)
#plt.show()

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope", slope)
print("intercept", intercept)
print("r", r)
print("p", p)
print("std_err", std_err)

def myfun(x):
    return slope * x + intercept
m = map(myfun, x)
print("m", m)
li = list(m)
print("li", li)
mymodel = li

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

predict = myfun(11)
print("predict", predict)
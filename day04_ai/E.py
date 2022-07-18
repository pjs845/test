# 선형 회귀 (Linear Regression) : Good Fit
import matplotlib.pyplot as plt
from scipy import stats

x = [6,8,9,8,3,18,3,10,5,12,13,10,7]
y = [100,87,88,89,112,87,104,88,95,79,78,86,87]

#plt.scatter(x,y)
#plt.show()

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope", slope) #기울기(가중치 weight)
print("intercept",intercept) #y절편 (편향 bias)
print("r", r) #점과 선의 관계 (Relationship)
print("p", p) #P값 (x,y 사이의 관계 지수) A low P-value (<0.05), High P-value (>0.05)
print("std_err", std_err) #표준오차 (Standard Error)
#a = b = c = stats.linregress(x, y)

def myfun(x):
    return slope * x + intercept
#mymodel = list(map(myfun, x))
m = map(myfun, x)
print("m", m)
li = list(m)
print("li", li)
mymodel = li


plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# 예측(Predict)
predict = myfun(11)
print("predict", predict)
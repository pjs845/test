# 선형 회귀(Linear Regression) : Bad Fit
import matplotlib.pyplot as plt
from scipy import stats

x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]

#plt.scatter(x, y)
#plt.show()

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope", slope) #기울기
print("intercept",intercept) #편향
print("r", r) #관계 (Relationship)
print("p", p)
print("std_err", std_err)

def myfun(x):
    return slope * x + intercept
mymodel = list(map(myfun, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#신뢰성 판단 계수
print("r", r) #0.0133
# 이 데이터는 Linear Regression을 적용하기에 무리!!
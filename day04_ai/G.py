# 다항 회귀(Polynomial Regression) : Good Fit
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [2,3,4,6,7,8,9,10,11,13,14,15,16,17,19,20,22,23]
y = [101,91,81,61,61,56,61,66,71,71,76,77,79,80,91,100,100,101]

#plt.scatter(x, y)
#plt.show()

a = np.polyfit(x, y, 3) # 3 => 3차식으로 fiting한 결과
mymodel = np.poly1d(a)
print("mymodel", mymodel)
myline = np.linspace(2, 23, 200) #(시작x값, 끝x값, 그 사이의 점 갯수)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(y, mymodel(x)) # 0(전혀관계X) <= r <= 1(100%관계O)
print("r", r2) #0.9432

predict = mymodel(18)
print("predict", predict)
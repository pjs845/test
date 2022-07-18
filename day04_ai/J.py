#모델 정확도를 측정 ( Train/Test )
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(200, 50, 100) / x
#print("x", x, "\ny", y)

#plt.scatter(x, y)
#plt.show()

train_x = x[:80] #0~399
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

#plt.scatter(train_x, train_y)
#plt.scatter(test_x, test_y)
#plt.show()

a = np.polyfit(train_x, train_y, 4)
mymodel = np.poly1d(a)
myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(train_y, mymodel(train_x))
print("r2(train)", r2)

r2 = r2_score(test_y, mymodel(test_x))
print("r2(test)", r2)

#예측
predict = mymodel(5)
print("predict", predict) #30.714150612104504
predict = mymodel(3)
print("predict", predict) #77.65400069836096
predict = mymodel(6)
print("predict", predict) #251.4665849095536
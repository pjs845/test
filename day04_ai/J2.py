import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(3)

x = np.random.normal(3,1,100)
y = np.random.normal(200, 50, 100)

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

a = np.polyfit(train_x, train_y, 4)
mymodel = np.poly1d(a)
myline = np.linspace(0,6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(train_y, mymodel(train_x))
print("r2(train)", r2)

r2 = r2_score(test_y, mymodel(test_x))
print("r2(test)", r2)

predict = mymodel(5)
print("predict", predict)
predict = mymodel(3)
print("predict", predict)
predict = mymodel(6)
print("predict", predict)
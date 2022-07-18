import pandas as pd
from sklearn import linear_model

df = pd.read_csv("자료실/cars1.csv")
col = ['Volume', 'Weight']
X = df[col]
y = df["CO2"]

lr = linear_model.LinearRegression()
lr.fit(X, y)

input = [2000, 1500]
predictCo2 = lr.predict([input])
print("predictCo2(1)", predictCo2)

print("lr.coef_", lr.coef_)

input = [3000, 1500]
predictCo2 = lr.predict([input])
print("predictCo2(2)", predictCo2)

input = [2000, 2500]
predictCo2 = lr.predict([input])
print("predictCo2(3)", predictCo2)

#멀티 회귀 ( Multiple Regression )

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("자료실/cars1.csv")
#print(df)
col = ['Volume', 'Weight']
X = df[col]
y = df['CO2']
#print(X)
#print(y)

lr = linear_model.LinearRegression()
lr.fit(X, y)

input = [2000, 1500]
predictCo2 = lr.predict([input]) # 차량(2000cc + 1500kg)
print("predictCo2(1)", predictCo2) # 106.63165525

print("lr.coef_", lr.coef_) #상관계수 [0.00780526 0.00755095]

input = [3000, 1500]
predictCo2 = lr.predict([input]) # 차량(3000cc + 1500kg)
print("predictCo2(2)", predictCo2) #114.43691278 
#(검증: 106.63165525 + (1000*0.00780526) = 114.43691)

input = [2000, 2500]
predictCo2 = lr.predict([input]) # 차량(2000cc + 2500kg)
print("predictCo2(3)", predictCo2) # 114.18260252 
#(검증: 106.63165525 + (1000 * 0.00755095) = 114.18260)
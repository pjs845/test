import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/awlst/Desktop/git/test/test/Report.xls')

result_age = df["분류"].loc[3:8]
result_data = df["전시회 관람"].loc[3:8]
age = np.array(result_age)
data = np.array(result_data)
#result = pd.Series(result, index=["10대", "20대", "30대", "40대", "50대", "60대 이상"])
#s1 = pd.Series(data, index=["10대", "20대", "30대", "40대", "50대", "60대 이상"])
print(result_age)
print(age)
print(data)

plt.bar(age, data)
plt.show()
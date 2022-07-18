import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

df = pd.read_excel('Report.xls')

result_age = df["분류"].loc[3:8]
result_data = df["전시회 관람"].loc[3:8]
age = np.array(result_age)
data = np.array(result_data)

plt.subplot(2,2,1)
plt.title("전시회 관람")
plt.bar(age, data)

result_age = df["분류"].loc[3:8]
result_data = df["박물관 관람"].loc[3:8]
age = np.array(result_age)
data = np.array(result_data)
plt.subplot(2,2,2)
plt.title("박물관 관람")
plt.bar(age, data)

result_loc = df["분류"].loc[21:25]
result_data = df["전시회 관람"].loc[21:25]
loc = np.array(result_loc)
data = np.array(result_data)
plt.subplot(2,2,3)
plt.title("지역별 전시회 관람")
plt.pie(data, labels=loc)

result_loc = df["분류"].loc[21:25]
result_data = df["박물관 관람"].loc[21:25]
loc = np.array(result_loc)
data = np.array(result_data)
plt.subplot(2,2,4)
plt.title("지역별 박물관 관람")
plt.pie(data, labels=loc)

plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

df = pd.read_csv("C:/Users/kosmo/Desktop/test/test/3. 공공자전거 대여소 정보(22.06월 기준).csv", encoding='cp949')
#print(df)
df["설치형태"].fillna(0, inplace=True)
df["Unnamed: 8"].fillna(0, inplace=True)
data = df["소재지(위치)"].loc[4:].value_counts()
location = np.array(data.index)
llist = len(location)
totarray = list()
result = 0
for x in range(0, int(llist)):
    for y in df.loc[df['소재지(위치)']==location[x]]["설치형태"].values:
        result += int(y)
    for z in df.loc[df['소재지(위치)']==location[x]]["Unnamed: 8"].values:
        try:
            result += int(z)
        except ValueError:
            pass
    
    totarray.append(result)
    result = 0
print(totarray)
plt.figure(figsize=(16,9))
plt.bar(location, totarray)
plt.xticks(fontsize=8)
plt.title("지역별 자전거 대여소 갯수", fontsize=25)
plt.show()

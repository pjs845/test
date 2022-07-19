import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

df = pd.read_csv("3. 공공자전거 대여소 정보(22.06월 기준).csv", encoding='cp949')
print(df)
df["설치형태"].fillna(0, inplace=True)
df["Unnamed: 8"].fillna(0, inplace=True)
#loc = np.array(df["소재지(위치)"].loc[4:].drop_duplicates())
#print(loc)

#for x in df["설치형태"].loc[4:]:
#    print(x)
#for x in df["Unnamed: 8"].loc[4:]:
#    print(x)
data = df["소재지(위치)"].loc[4:].value_counts()
location = np.array(data.index)
print(data)
print(location)
ld = df.loc[df['소재지(위치)']==location[0]]["설치형태"]
rd = df["Unnamed: 8"].loc[4:].values
llist = len(location)
print(llist)
for x in range(1, int(llist)+1):
    print()
    
#print(ld)
#print(rd)


'''
plt.figure(figsize=(16,9))
plt.bar(loc, data)
plt.xticks(fontsize=8)
plt.title("지역별 자전거 대여소 갯수", fontsize=25)
plt.show()
'''
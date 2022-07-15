import pandas as pd

#(1)읽기
df = pd.read_csv("자료실/dirtydata.csv")
print(df.to_string())
print()

#empty cell 제거
#df2 = df.dropna() # empty cell을 가진 row들을 제거해서 df생성
df2 = df.dropna()
print(df2.to_string())
print()

df.dropna(inplace=True) #원본의 df에서 empty cell을 가진 row를 제거함
print(df.to_string())
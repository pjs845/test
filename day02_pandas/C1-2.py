import pandas as pd

#DataFrame 2차원 테이블 데이터 구조
a = {
    "calories": [400, 300, 350],
    "duration": [50, 35, 45]
}
df1 = pd.DataFrame(a)
print(df1)
print()
print(df1.loc[1])
print()
print(df1.loc[[0,1]])
print()

df2 = pd.DataFrame(a, index=["d1", "d2", "d3"])
print(df2)
print(df2.loc["d2"])
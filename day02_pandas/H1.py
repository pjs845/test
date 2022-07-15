import pandas as pd

df = pd.read_csv("자료실/dirtydata.csv")
print(df.to_string())
print()

#empty cell 제거
df2 = df.dropna()
print(df2.to_string())
print()

df.dropna(inplace=True)
print(df.to_string())
import pandas as pd

df = pd.read_csv('자료실/data.csv')
print(df.to_string())
print()

x = df.corr()
print(x)
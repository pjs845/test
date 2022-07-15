import pandas as pd

# Wrong format 변경
df = pd.read_csv('자료실/dirtydata.csv')
print(df.to_string())
print()

df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
print()

df.dropna(subset=['Date'], inplace=True)
print(df.to_string())
print()
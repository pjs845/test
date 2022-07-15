import pandas as pd

df = pd.read_csv("자료실/dirtydata.csv")
print(df.to_string())
print()

print(df.duplicated())
print()

df.drop_duplicates(inplace=True)
print(df.to_string())
print()
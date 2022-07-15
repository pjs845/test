import pandas as pd

#empty cell 채움
df = pd.read_csv("자료실/dirtydata.csv")
print(df.to_string())
print()

#df.fillna(200, inplace=True)
#print(df.to_string())
#print()

#df["Calories"].fillna(200, inplace=True)
#print(df.to_string())
#print()

#x = df["Calories"].median()
#x = df["Calories"].mean()
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
print()

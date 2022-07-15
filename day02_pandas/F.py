import pandas as pd

# (1) 읽기
df = pd.read_excel("자료실/data.xlsx", engine="openpyxl")
print(df)

df.set_index('Duration', inplace=True)
print(df)

# (2) 쓰기
df.to_csv("자료실/output/data_xlsx.csv")
#df.to_json("자료실/output/data_xlsx.json")

#(3) 기타 엑셀 읽기 테스트
df1 = pd.read_excel("", engine="openpyxl")
print(df)
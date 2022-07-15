import pandas as pd

#(1) 읽기
df = pd.read_csv("C:\PJS\PyAdvanced\day02\자료실\data.csv")
#print(df.to_string()) #전체row
#print(df) # header 5, tailer 5

#print(pd.options.display.max_rows)
pd.options.display.max_rows = 169
pd.options.display.max_rows = 168
print(df)

df.set_index("Duration", inplace=True)
print(df)

#(2) 쓰기
df.to_excel("자료실\output\data_json.xlsx")
#df.to_json("자료실\output\data_csv.json")
import pandas as pd

#(1) 읽기
df = pd.read_csv("자료실/data.csv")
#print(df.to_string()) #전체 row 출력
#print(df) # header 5개, tailer 5개 출력

#print(pd.options.display.max_rows) #그냥 참고: 디스플레이에서 최대 row의 갯수
pd.options.display.max_rows = 169 # 총 row 갯수가 169개이므로 모두 출력
pd.options.display.max_rows = 168 # 총 row 갯수(169개)보다 적으므로 header와 tailer로 나눠 출력
print(df) #head tail 각각 5개씩 출력
print(df.head(10)) #head를 10개 출력
print(df.tail(10)) #tail을 10개 출력
print(df.head()) #head를 5개 출력
print(df.tail()) #tail을 5개 출력
print(df.info()) #df의 컬럼정보와 데이터타입 출력 >> oralcle의 desc와 비슷

df.set_index("Duration", inplace=True)
print(df)

#(2) 쓰기
df.to_excel("자료실/output/data_json.xlsx")
#df.to_json("자료실/output/data_csv.json")
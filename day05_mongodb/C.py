from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
#print(mgClient)
mgDb = mgClient["mydatabase"]
mgCol = mgDb["customers"]

mgDic = {"name":"soo", "addr":"seoul"} #JSON
x = mgCol.insert_one(mgDic)
print(x.inserted_id) # _id 컬럼이 자동으로 생성되어 해시코드값이 자동 입력됨 primary key 62d5164be4c611086f0631d2
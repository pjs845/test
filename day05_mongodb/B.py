from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
#print(mClient)
mgDb = mgClient["mydatabase"]
myCol = mgDb["customers"]

colList = mgDb.list_collection_names()
print(colList)
if "customers" in colList:
    print("customers 컬렉션 존재") #Collection에 내용이 입력되기 전까지는 생성되지 않음
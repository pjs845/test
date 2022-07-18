from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
print(mgClient)
mgDb = mgClient["mydatabase"]
myCol = mgDb["customers"]

colList = mgDb.list_collection_names()
print(colList)
if "customers" in colList:
    print("customers 컬렉션 존재")
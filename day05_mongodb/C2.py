from pymongo import mongo_client
url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
#print(mgClient)
mgDb = mgClient["mydatabase"]
myCol = mgDb["customers"]

mgDic = {"name":"soo", "addr":"seoul"}
x = myCol.insert_one(mgDic)
print(x.inserted_id)
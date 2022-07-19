from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
print(mgClient)
db = mgClient["parkdb"]
col = db["address"]

import datetime
dt_now = datetime.datetime.now()
print("dt.now", dt_now)
print(type(dt_now))

dic = {"name":"길동", "addr":"부산", "rdate":dt_now} #JSON Format
row = col.insert_one(dic)
print("row.inserted_id", row.inserted_id)

doc = col.find_one()
print(doc)
print()

#docs = col.find()
#docs = col.find().sort("_id")
#docs = col.find().sort("_id",-1)
#docs = col.find().sort("name")
#docs = col.find().sort("name",-1)
docs = col.find().sort("rdate", -1)
for doc in docs:
    print(doc)

col.drop()
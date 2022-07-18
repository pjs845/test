from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
print(mgClient)
mgDb = mgClient["mydatabase"]
print(mgDb)

dblist = mgClient.list_database_names()
print(dblist)

if "mydatabase" in dblist:
    print("mydatabase 존재함")
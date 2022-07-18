from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
#print(mClient)
mgDb = mgClient["mydatabase"]
#print(mgDb)

dblist = mgClient.list_database_names()
#print(dblist)

if "mydatabase" in dblist:
    print("mydatabase 존재함") #DB에 내용이 입력되기 전까지는 생성되지 않음

    
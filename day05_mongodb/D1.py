from pymongo import mongo_client

url = "mongodb://localhost:27017"
mgClient = mongo_client.MongoClient(url)
db = mgClient["parkdb"]
col = db["address"]

import datetime
dt_now = datetime.datetime.now()

dics = [
  { "_id":1, "name": "가길동", "addr": "서울", "rdate":dt_now},
  { "_id":2, "name": "나길동", "addr": "경기", "rdate":dt_now},
  { "_id":3, "name": "다길동", "addr": "부산", "rdate":dt_now},
  { "_id":4, "name": "라길동", "addr": "인천", "rdate":dt_now},
  { "_id":5, "name": "마길동", "addr": "대구", "rdate":dt_now},
  { "_id":6, "name": "바길동", "addr": "광주", "rdate":dt_now},
  { "_id":7, "name": "사길동", "addr": "대전", "rdate":dt_now},
  { "_id":8, "name": "아길동", "addr": "울산", "rdate":dt_now},
  { "_id":9, "name": "자길동", "addr": "창원", "rdate":dt_now},
  { "_id":10, "name": "차길동", "addr": "청주", "rdate":dt_now}
]
#rows = col.insert_many(dics)
#print("rows.inserted_ids", rows.inserted_ids)

#docs = col.find()
#for doc in docs:
#    print(doc)

#docs = col.find({}, {"_id":1})
#for doc in docs:
#    print(doc)

#docs = col.find({}, {"_id":0})
#for doc in docs:
#    print(doc)

#docs = col.find({}, {"_id":1, "name":1})
#for doc in docs:
#    print(doc)

#docs = col.find({}, {"name":1, "addr":1})
#for doc in docs:
#    print(doc)

#docs = col.find({}, {"name":1, "addr":0}) #"addr":0는 error
#for doc in docs:
#    print(doc)

# "_id":1가 디폴트
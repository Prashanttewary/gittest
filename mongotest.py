import pymongo
client = pymongo.MongoClient("mongodb+srv://prashanttewary:leecooper@cluster1979.ul9dzmh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"Prashant",
    "email" : "prashant.tewary79@gmail.com",
    "surname" : "Tewary"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

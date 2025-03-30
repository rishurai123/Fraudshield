import json
import pymongo


MONGO_URI = "mongodb://localhost:27017/" 
DB_NAME = "mydb" 
COLLECTION_NAME = "transactions"  


with open("transactions.json", "r") as file:
    data = json.load(file)


client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


if "transactions" in data:
    collection.insert_many(data["transactions"])
    print(f"✅ Successfully imported {len(data['transactions'])} transactions into MongoDB.")


client.close()




from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.dp2
# specify a collection
collection = db.projectdata


directory = "data"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as file:
        try:
            file_data = json.load(file)
           

            try:
                collection.insert_many(file_data)
        
            except Exception as e:
                print(e, "Error with importing")

        except Exception as e:
                print("Exception", e, filename)



   
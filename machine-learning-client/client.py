import time
import random
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client.ml_data

def generate_data():
    db.data.delete_many({})
    while True:
        data = {
            "sensor": "camera",
            "value": random.randint(1, 100)
        }
        db.data.insert_one(data)
        print(f"Inserted data: {data}")
        time.sleep(5) 

if __name__ == "__main__":
    generate_data()



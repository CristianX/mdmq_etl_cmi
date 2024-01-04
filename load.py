import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def load_data(data, mongo_uri):
    if not data:
        return

    client = MongoClient(mongo_uri)
    db = client[os.environ.get("MONGO_BDD_NAME")]

    system_name = data[0]["SISTEMA"]
    collection = db[system_name]

    collection.insert_many(data)

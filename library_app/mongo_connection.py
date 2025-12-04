from pymongo import MongoClient
from django.conf import settings

def get_db():
    client = MongoClient(settings.MONGO_DB["URI"])
    db = client[settings.MONGO_DB["NAME"]]

    
    db["books"].create_index("title")
    db["members"].create_index("name")

    return db

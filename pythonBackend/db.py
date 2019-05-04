from pymongo import MongoClient

client = MongoClient()
db = client['test_db']


def insert(value, collection):
    col = db['tweets']

    insert_id = col.update({'_id': value['_id']}, value, upsert=True)
    return insert_id

def update(value, collection):
    col = db['tweets']
    insert_id = col.update({'_id': value['_id']}, value, upsert=True)
    return insert_id


def search(key, collection):
    col = db['tweets']
    data = col.find_one(key)
    return data




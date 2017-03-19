from flask_pymongo import PyMongo
from hashlib import blake2b
from json import dumps

mongo = PyMongo()


def gen_id(data):
    m = blake2b()
    m.update(dumps(data).encode())
    return m.hexdigest()[:32]


def get_links():
    return mongo.db.links.find()


def get_link(id):
    return mongo.db.links.find_one({'_id': id})


def create_link(data):
    data['_id'] = gen_id(data)
    result = mongo.db.links.insert_one(data)
    if result.acknowledged:
        return mongo.db.links.find_one({'_id': result.inserted_id})
    else:
        raise Exception('Insert failed')


def update_link(id, data):
    result = mongo.db.links.update_one({'_id': id}, {'$set': data})
    if result.acknowledged:
        return mongo.db.links.find_one({'_id': id})
    else:
        raise Exception('Update failed')


def delete_link(id):
    result = mongo.db.links.delete_one({'_id': id})
    return {'deleted': true}

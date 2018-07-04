__author__ = "abhishekmadhu"

import pymongo

# contains functions that can be used in the Database


class Database(object):
    URI = "mongodb://127.0.0.1:27017"  # keeping these same for all db
    DATABASE = None

    @staticmethod   # to not use self, as this belongs to whole db class and not to a single instance only
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fulllstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, data):
        return Database.DATABASE[collection].find(data)

    @staticmethod
    def find_one(collection, data):
        return Database.DATABASE[collection].find_one(data)
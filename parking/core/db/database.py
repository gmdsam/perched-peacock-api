import pymongo


class Database:

    def __init__(self):
        self._db = None

    def handshake(self, url, db_name):
        self._db = pymongo.MongoClient(url)[db_name]
        return self._db

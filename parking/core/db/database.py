import pymongo


class Database:

    def __init__(self):
        self._db = None

    def handshake(self, url):
        self._db = pymongo.MongoClient(url)['PerchedPeacock']
        return self._db

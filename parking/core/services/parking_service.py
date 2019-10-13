from injector import inject
import uuid

from parking.core.models.parking_lot import ParkingLotModel


class ParkingService:

    @inject
    def __init__(self, db):
        self._db = db

    def generate_parking_lot(self, parking_lot):
        self._db['ParkingLots'].drop()
        self._db['ParkingLots'].insert_many(parking_lot)

    def get_parking_db(self):
        cursor = self._db['ParkingLots'].find({})
        parking_lot = []
        for document in cursor:
            parking_lot.append({'locality': document['Locality'], 'city': document['City']})
        return parking_lot

    def create_parking_lot(self, locality, city, country, capacity):
        self._db['ParkingLots'].insert({'ID': uuid.uuid4(), 'Locality': locality, 'City': city, 'Country': country,
                                        'Capacity': capacity})

    def get_parking_lot(self, locality, city, country):
        parking_lot = self._db['ParkingLots'].find_one({'Locality': locality, 'City': city, 'Country': country})
        return ParkingLotModel(parking_lot['ID'], parking_lot['Locality'], parking_lot['City'], parking_lot['Country'],
                               parking_lot['Capacity'])

    def availability(self, parking_entry, parking_lot):
        pass

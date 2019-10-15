from injector import inject
import uuid
from datetime import datetime
import time

from parking.core.models.parking_lot import ParkingLotModel


class ParkingService:

    @inject
    def __init__(self, db):
        self._db = db

    def populate_parking_db(self, parking_lot):
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

    def get_parking_lot(self, locality, city):
        parking_lot = self._db['ParkingLots'].find_one({'Locality': locality, 'City': city})
        return ParkingLotModel(parking_lot['ID'], parking_lot['Locality'], parking_lot['City'], parking_lot['Country'],
                               parking_lot['Capacity'])

    def availability(self, parking_entry, parking_lot):
        parking_lot_collection = parking_lot._locality + '_' + parking_lot._city + '_' + parking_lot._country
        arrival_date = datetime.strptime(parking_entry._arrival_date, '%a %b %d %Y')
        departure_date = datetime.strptime(parking_entry._departure_date, '%a %b %d %Y')
        arrival_time = parking_entry._arrival_time
        departure_time = parking_entry._departure_time
        occupied = self._db[parking_lot_collection].count_documents({'arrivalDate': {'$lt': str(departure_date.date())},
                                                          'departureDate': {'$gt': str(arrival_date.date())},
                                                          'arrivalTime': {'$lt': departure_time},
                                                          'departureTime': {'$gt': arrival_time}})
        if occupied >= parking_lot._capacity['Car']:
            return False
        return True

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
        date = datetime.strptime(parking_entry._arrival_date, '%a %b %d %Y')
        arrival_date = str(date.year) + ' ' + str(date.month) + ' ' + str(date.day)
        date = datetime.strptime(parking_entry._departure_date, '%a %b %d %Y')
        departure_date = str(date.year) + ' ' + str(date.month) + ' ' + str(date.day)
        arrival_time = parking_entry._arrival_time
        departure_time = parking_entry._departure_time
        occupied = self._db[parking_lot_collection].count_documents({'ArrivalDate': {'$lte': departure_date},
                                                                     'DepartureDate': {'$gte': arrival_date},
                                                                     'ArrivalTime': {'$lte': departure_time},
                                                                     'DepartureTime': {'$gte': arrival_time}})
        if occupied >= parking_lot._capacity['Car']:
            return False
        return True

    def book(self, parking_entry, parking_lot):
        if self.availability(parking_entry, parking_lot):
            parking_lot_collection = parking_lot._locality + '_' + parking_lot._city + '_' + parking_lot._country
            date = datetime.strptime(parking_entry._arrival_date, '%a %b %d %Y')
            arrival_date = str(date.year) + ' ' + str(date.month) + ' ' + str(date.day)
            date = datetime.strptime(parking_entry._departure_date, '%a %b %d %Y')
            departure_date = str(date.year) + ' ' + str(date.month) + ' ' + str(date.day)
            self._db[parking_lot_collection].insert({'VehicleNumber': parking_entry._vehicle_number,
                                                     'ArrivalDate': arrival_date,
                                                     'ArrivalTime': parking_entry._arrival_time,
                                                     'DepartureDate': departure_date,
                                                     'DepartureTime': parking_entry._departure_time,
                                                     'Locality': parking_lot._locality,
                                                     'City': parking_lot._city,
                                                     'Country': parking_lot._country})
            return True
        else:
            return False

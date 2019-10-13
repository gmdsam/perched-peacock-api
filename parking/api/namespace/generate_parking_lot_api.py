from flask import Response
from flask_restplus import Resource, Namespace
import uuid
from injector import inject
import json

from parking.core.services.parking_service import ParkingService

api = Namespace('generateParkingLot')


@api.route('')
class GenerateParkingLotApi(Resource):

    @inject
    def __init__(self, parking_service: ParkingService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parking_service = parking_service

    def get(self):
        parking_lot = self.__parking_service.get_parking_db()
        r = Response(response=json.dumps(parking_lot), status=200)
        return r

    def post(self):
        parking_lot = [
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Bangalore', 'Locality': 'Whitefield',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Bangalore', 'Locality': 'Kormangala',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Bangalore', 'Locality': 'Indiranagar',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Bangalore', 'Locality': 'Malleshwaram',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Mumbai', 'Locality': 'Borivali',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Mumbai', 'Locality': 'Bandra',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Mumbai', 'Locality': 'Thane',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Delhi', 'Locality': 'Rajiv Chowk',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Delhi', 'Locality': 'GB Road',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'India', 'City': 'Delhi', 'Locality': 'Hauz Khas',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Chicago', 'Locality': 'Lincoln Square',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Chicago', 'Locality': 'Riverdale',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Chicago',
             'Locality': 'Washington Heights', 'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Chicago', 'Locality': 'Uptown',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Los Angeles',
             'Locality': 'Santa Monica', 'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Los Angeles',
             'Locality': 'Beverly Hills', 'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'Los Angeles', 'Locality': 'Pasadena',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'New York', 'Locality': 'Manhattan',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'New York', 'Locality': 'Queens',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United States of America', 'City': 'New York', 'Locality': 'Brooklyn',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'London', 'Locality': 'Greenwich',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'London', 'Locality': 'Havering',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'London', 'Locality': 'Bromley',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'London', 'Locality': 'Westminster',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Liverpool', 'Locality': 'Canning',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Liverpool', 'Locality': 'Fairfield',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Liverpool', 'Locality': 'Kensington',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Birmingham', 'Locality': 'Bournville',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Birmingham', 'Locality': 'Springfield',
             'Capacity': {'Bike': 10, 'Car': 5}},
            {'ID': uuid.uuid4(), 'Country': 'United Kingdom', 'City': 'Birmingham', 'Locality': 'Vauxhall',
             'Capacity': {'Bike': 10, 'Car': 5}}
        ]
        self.__parking_service.generate_parking_lot(parking_lot)
        r = Response(response='Parking lot information added', status=200)
        return r

from flask import request, Response
from flask_restplus import Resource, Namespace
import logging
from injector import inject

from parking.api.error_handler import error_handler
from parking.core.models.parking_entry import ParkingEntryModel
from parking.core.services.parking_service import ParkingService

api = Namespace('park')


@api.route('')
class ParkingSpace(Resource):

    @inject
    def __init__(self, parking_service: ParkingService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parking_service = parking_service

    @error_handler
    def get(self):
        data = request.form.to_dict()
        arrival = data['arrival']
        departure = data['departure']
        vehicle_type = data['vehicleType']
        locality = data['locality']
        city = data['city']
        country = data['country']

        parking_lot = self.__parking_service.get_parking_lot(locality, city, country)
        parking_entry = ParkingEntryModel(arrival, departure, vehicle_type)
        if self.__parking_service.availability(parking_entry, parking_lot):
            r = Response(response=True)
        else:
            r = Response(response=False)
        return r

    @error_handler
    def post(self):
        data = request.form.to_dict()
        arrival = data['arrival']
        departure = data['departure']
        vehicle_type = data['vehicleType']
        vehicle_number = data['vehicleNumber']
        locality = data['locality']
        city = data['city']
        country = data['country']

        parking_lot = self.__parking_service.get_parking_lot(locality, city, country)
        parking_entry = ParkingEntryModel(arrival, departure, vehicle_type, vehicle_number)
        if self.__parking_service.availability(parking_entry, parking_lot):
            r = Response(response=True)
        else:
            r = Response(response=False)
        return r

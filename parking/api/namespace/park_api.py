from flask import request, Response
from flask_restplus import Resource, Namespace
import logging
from injector import inject
import json_tricks

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
        data = request.args.to_dict()
        # print(data)
        # return Response(status=200)
        arrival_date = data['arrivalDate']
        arrival_time = data['arrivalTime']
        departure_date = data['departureDate']
        departure_time = data['departureTime']
        vehicle_type = data['vehicleType']
        locality = data['locality']
        city = data['city']
        parking_lot = self.__parking_service.get_parking_lot(locality, city)
        parking_entry = ParkingEntryModel(arrival_date, arrival_time, departure_date, departure_time, vehicle_type)
        if self.__parking_service.availability(parking_entry, parking_lot):
            r = Response(response=json_tricks.dumps(True), status=200)
            r.mimetype = 'application/json'
        else:
            r = Response(response=json_tricks.dumps(False), status=200)
            r.mimetype = 'application/json'
        return r

    @error_handler
    def post(self):
        data = request.form.to_dict()
        arrival_date = data['arrivalDate']
        arrival_time = data['arrivalTime']
        departure_date = data['departureDate']
        departure_time = data['departureTime']
        vehicle_type = data['vehicleType']
        vehicle_number = data['vehicleNumber']
        locality = data['locality']
        city = data['city']
        country = data['country']

        parking_lot = self.__parking_service.get_parking_lot(locality, city)
        parking_entry = ParkingEntryModel(arrival_date, arrival_time, departure_date, departure_time, vehicle_type, vehicle_number)
        if self.__parking_service.availability(parking_entry, parking_lot):
            r = Response(response=json_tricks.dumps(True), status=200)
            r.mimetype = 'application/json'
        else:
            r = Response(response=json_tricks.dumps(False), status=200)
            r.mimetype = 'application/json'
        return r

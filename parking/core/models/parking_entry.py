class ParkingEntryModel:

    def __init__(self, arrival_date, arrival_time, departure_date, departure_time, vehicle_type, vehicle_number=None):
        self._arrival_date = arrival_date
        self._arrival_time = arrival_time
        self._departure_date = departure_date
        self._departure_time = departure_time
        self._vehicle_type = vehicle_type
        self._vehicle_number = vehicle_number

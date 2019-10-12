class ParkingEntryModel:

    def __init__(self, arrival, departure, vehicle_type, vehicle_number=None):
        self._arrival = arrival
        self._departure = departure
        self._vehicle_type = vehicle_type
        self._vehicle_number = vehicle_number

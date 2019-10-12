from flask_restplus import Api
from .authenticate_api import api as ns_authenticate
from .park_api import api as ns_park
from .generate_parking_lot_api import api as ns_generate_parking_lot

API_PREFIX = '/pp/v1'

# authorizations = {}

api = Api()
api.add_namespace(ns_authenticate, path=API_PREFIX+'/authenticate')
api.add_namespace(ns_generate_parking_lot, path=API_PREFIX+'/generateParkingLot')
api.add_namespace(ns_park, path=API_PREFIX+'/park')

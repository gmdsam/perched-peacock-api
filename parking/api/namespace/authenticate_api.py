from flask import request
from flask_restplus import Resource, Namespace
from parking.api.error_handler import error_handler
import logging

api = Namespace('/authenticate')


@api.route('/login')
class Login(Resource):

    @error_handler
    def post(self):
        logging.getLogger().info({
            'Login': 'Successful'
        })


@api.route('/signup')
class SignUp(Resource):

    @error_handler
    def post(self):
        logging.getLogger().info({
            'SignUp': 'Successful'
        })

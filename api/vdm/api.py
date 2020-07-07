from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
import config
import utilities

app = Flask(__name__)
api = Api(app=app, version='0.1.0', title='VDM Api',
          description='Awesome API', validate=True)


ns_root = api.namespace('/', description="root")
ns_reservation = api.namespace('reservation', description="reservation stuff")
ns_reservations = api.namespace('reservations',
                                description="reservations stuff")


@ns_root.route('/')
class default_root(Resource):
    def get(self):
        """Index."""
        return "Welcome to VDM escape game\n"


@ns_reservation.route("")
class Reservation(Resource):
    """Reservation related operations."""

    def post(self):
        """reservation booking data."""
        vdm_database = config.setup_mongo()
        collection = vdm_database["booking"]

        data = utilities.handle_prices(request.get_json())
        collection.insert_one(data)

        response = jsonify({'message': 'OK'})
        response.status_code = 201
        return response


@ns_reservations.route("")
class Reservations(Resource):
    def get(self):
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.find({}, {"_id": 0})
        data = []
        for reservation in cursor:
            data.append(reservation)

        response = jsonify(data)
        response.status_code = 200
        return response

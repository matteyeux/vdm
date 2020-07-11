import json
from flask import jsonify, request
from flask_restplus import Namespace, Resource
from bson.json_util import dumps
from bson.objectid import ObjectId

import config
import utilities

ns_reservations = Namespace('reservations', description="reservations stuff")
ns_reservation = Namespace('reservation', description="reservation stuff")
ns_bookingList = Namespace('bookingList', description="booking list stuff")
ns_incrementBookingList = Namespace('incrementBookingList',
                                    description="incremental booking \
                                                   list stuff")


@ns_reservation.route("")
class Reservation(Resource):
    """Reservation related operations."""

    def post(self):
        """reservation booking data."""
        vdm_database = config.setup_mongo()
        collection = vdm_database["booking"]

        # data = utilities.handle_prices(request.get_json())
        data = utilities.handle_utilities(request.get_json())
        collection.insert_one(data)

        response = jsonify({'message': 'OK'})
        response.status_code = 201
        return response


@ns_reservations.route("")
class Reservations(Resource):
    def get(self):
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.find({}, {'_id': 0}).sort("_id", -1)
        data = []
        for reservation in cursor:
            data.append(reservation)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_bookingList.route("/")
class BookingList(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "_id": 1,
                    "Acheteur.Nom": 1,
                    "Acheteur.Prenom": 1,
                    "NbSpectateur": {"$size": "$Reservation"},
                    "Game.Nom": 1,
                    "Game.Jour": 1,
                    "TotalPrice": {"$sum": "$Reservation.prix"}
                }
            },
            {"$sort": {"_id": 1}},
            {"$limit": 100}
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_incrementBookingList.route("/")
class IncrementBookingList(Resource):
    def get(self):
        """Get incremental bookinglist information."""
        lastId = request.args.get('lastId')
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "_id": 1,
                    "Acheteur.Nom": 1,
                    "Acheteur.Prenom": 1,
                    "NbSpectateur": {"$size": "$Reservation"},
                    "Game.Nom": 1,
                    "Game.Jour": 1,
                    "TotalPrice": {"$sum": "$Reservation.prix"}
                }
            },
            {"$match": {"_id": {"$gt": ObjectId(lastId)}}},
            {"$limit": 50}
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response
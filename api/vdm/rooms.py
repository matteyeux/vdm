import json
from flask import jsonify
from bson.json_util import dumps
from flask_restplus import Namespace, Resource
import config


ns_caRoomDays = Namespace('caRoomDays', description="CA per rooms and days")
ns_cadRoom = Namespace('cadRoom', description="CAD per rooms")


@ns_caRoomDays.route("/")
class CaRoomDays(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "date": {"$dateToString": {"format": "%d/%m/%Y",
                                               "date": "$CreatedAt"}},
                    "Game.Nom": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"date": "$date", "Room": "$Game.Nom"},
                    "CA": {"$sum": "$CA"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            },
            {
                "$group": {
                    "_id": "$_id.date",
                    "Rooms": {"$push": {
                        "Room": "$_id.Room",
                        "CA": "$CA",
                        "Nb_Spec": "$Nb_Spec",
                    }}
                }
            },
            {"$sort": {"_id": 1}},
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_cadRoom.route("/")
class CadRoom(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.Nom": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"Rooms": "$Game.Nom"},
                    "CA": {"$sum": "$CA"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            },
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response

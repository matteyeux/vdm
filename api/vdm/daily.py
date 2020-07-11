import json
from bson.json_util import dumps
from flask import jsonify
from flask_restplus import Namespace, Resource
import config


ns_caDays = Namespace('caDays', description="CA per day")
ns_nbBookingDays = Namespace('nbBookingDays',
                             description="Number of bookings per days")
ns_nbSpectDays = Namespace('nbSpectDays',
                           description="Number of spectators per days")


@ns_caDays.route("/")
class CADays(Resource):
    def get(self):
        """Get CA and Nb Booking per days."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "date": {"$dateToString": {"format": "%d/%m/%Y",
                                               "date": "$CreatedAt"}},
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Booking": {"$sum": 1}
                }
            },
            {"$sort": {"_id": 1}},
            {
                "$group": {
                    "_id": "$date",
                    "CA": {"$sum": "$CA"},
                    "Nb_Booking": {"$sum": "$Nb_Booking"}
                }
            }
        ])

        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_nbBookingDays.route("/")
class NbBookingDays(Resource):
    def get(self):
        """Get Nb Booking and Nb Spect per days."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "date": {"$dateToString": {"format": "%d/%m/%Y",
                                               "date": "$CreatedAt"}},
                    "Nb_Booking": {"$sum": 1},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {"$sort": {"_id": 1}},
            {
                "$group": {
                    "_id": "$date",
                    "Nb_Booking": {"$sum": "$Nb_Booking"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            }
        ])

        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_nbSpectDays.route("/")
class NbSpectDays(Resource):
    def get(self):
        """Get CA and Nb Spect per days."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "date": {"$dateToString": {"format": "%d/%m/%Y",
                                               "date": "$CreatedAt"}},
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {"$sort": {"_id": 1}},
            {
                "$group": {
                    "_id": "$date",
                    "CA": {"$sum": "$CA"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            }
        ])

        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response

import json
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_extractKPIDaily = Namespace('extractKPIDaily', description="Daily KPI to extract")
ns_extractKPIHisto = Namespace('extractKPIHisto', description="Historic KPI to extract")


@ns_extractKPIDaily.route("/")
class ExtractKPIDaily(Resource):
    def get(self):
        """Get daily KPI to extract with cronjob."""
        now = datetime.now()
        gen_time = datetime(now.year, now.month, now.day)
        dummy_id = ObjectId.from_datetime(gen_time)

        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                    {
                        "_id": 1,
                        "date": {"$dateToString": {"format": "%d/%m/%Y",
                                                   "date": "$CreatedAt"}},
                        "CA": {"$sum": "$Reservation.prix"},
                        "NbBooking": {"$sum": 1},
                        "NbSpect": {"$size": "$Reservation"},
                    },
            },
            {"$match": {"_id": {"$gte": dummy_id}}},
            {
                "$group": 
                    {
                        "_id": "$date",
                        "CA": {"$sum": "$CA"},
                        "Nb Reservations": {"$sum": "$NbBooking"},
                        "Nb Spectateurs": {"$sum": "$NbSpect"},
                    }
            },
            {
                "$project":
                    {
                        "Date": "$_id",
                        "_id": 0,
                        "CA": 1,
                        "Nb Reservations": 1,
                        "Nb Spectateurs": 1,
                        "Prix Moyen Reservation (€)": {"$round": 
                            [{"$divide": 
                            ["$CA", {"$sum": "$Nb Reservations"}]}, 2]},
                        "Ticket Moyen Spectateur (€)": {"$round": 
                            [{"$divide": 
                            ["$CA", {"$sum": "$Nb Spectateurs"}]}, 2]},
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


@ns_extractKPIHisto.route("/")
class ExtractKPIHisto(Resource):
    def get(self):
        """Get Hitoric KPI to extract with cronjob."""
        now = datetime.now()
        gen_time = datetime(now.year, now.month, now.day)
        dummy_id = ObjectId.from_datetime(gen_time)

        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                    {
                        "_id": 1,
                        "date": {"$dateToString": {"format": "%d/%m/%Y",
                                                   "date": "$CreatedAt"}},
                        "CA": {"$sum": "$Reservation.prix"},
                        "NbBooking": {"$sum": 1},
                        "NbSpect": {"$size": "$Reservation"},
                    },
            },
            {"$match": {"_id": {"$lt": dummy_id}}},
            {"$sort": {"_id": 1}},
            {
                "$group": 
                    {
                        "_id": "$date",
                        "CA": {"$sum": "$CA"},
                        "Nb Reservations": {"$sum": "$NbBooking"},
                        "Nb Spectateurs": {"$sum": "$NbSpect"},
                    }
            },
            {
                "$project":
                    {
                        "Date": "$_id",
                        "_id": 0,
                        "CA": 1,
                        "Nb Reservations": 1,
                        "Nb Spectateurs": 1,
                        "Prix Moyen Reservation (€)": {"$round": 
                            [{"$divide": 
                            ["$CA", {"$sum": "$Nb Reservations"}]}, 2]},
                        "Ticket Moyen Spectateur (€)": {"$round": 
                            [{"$divide": 
                            ["$CA", {"$sum": "$Nb Spectateurs"}]}, 2]},
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
import json
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_dailyKPI = Namespace('dailyKPI', description="Daily KPI")
ns_kpi = Namespace('kpi', description="KPI")


@ns_dailyKPI.route("/")
class DailyKPI(Resource):
    def get(self):
        """Get Daily KPi."""
        now = datetime.now()
        gen_time = datetime(now.year, now.month, now.day)
        dummy_id = ObjectId.from_datetime(gen_time)

        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                    {
                        "_id": 1,
                        "NbSpectateur": {"$size": "$Reservation"},
                        "TotalPrice": {"$sum": "$Reservation.prix"}
                    },
            },
            {"$match": {"_id": {"$gte": dummy_id}}},
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_kpi.route("/")
class KPI(Resource):
    def get(self):
        """Get KPi."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "_id": 1,
                    "NbSpectateur": {"$size": "$Reservation"},
                    "TotalPrice": {"$sum": "$Reservation.prix"}
                },
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

import json
from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_buyerSex = Namespace('buyerSex', description="Histo split man / wooman")
ns_buyerSexDaily = Namespace('buyerSexDaily', description="Daily split man / wooman")

ns_customer_civilities = Namespace('customer/civilities', description="statistics stuff")
ns_customer_civilities_daily = Namespace('customer/civilities/daily', description="statistics stuff")

ns_spectatorsSex = Namespace('spectatorsSex', description="Histo split man / wooman")
ns_spectatorsSexDaily = Namespace('spectatorsSexDaily', description="Daily split man / wooman")

ns_buyerVR = Namespace('buyerVR', description="Histo split VR / Not VR")
ns_buyerVRDaily = Namespace('buyerVRDaily', description="Daily split VR / Not VR")
ns_spectatorsVR = Namespace('spectatorsVR', description="Histo split VR / Not VR")
ns_spectatorsVRDaily = Namespace('spectatorsVRDaily', description="Daily split VR / Not VR")

ns_buyerBookingsHours = Namespace('buyerHours', description="dispatch buyer by hours")
ns_spectatorsBookingsHours = Namespace('spectatorsHours', description="dispatch Spectators by hours")

ns_buyerGamehours = Namespace('buyerGameHours', description="dispatch buyer by Games hours")
ns_spectatorsGamehours = Namespace('spectatorsGameHours', description="dispatch Spectators by Games hours")

ns_buyerSplitAge = Namespace('buyerhours', description="dispatch buyer by hours")
ns_spectatorsSplitAge = Namespace('spectatorshours', description="dispatch Spectators by hours")
@ns_customer_civilities.route("")
class CustomerCivility(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Acheteur.Civilite": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": "$Acheteur.Civilite",
                    "total": {"$sum": "$Nb"}
                }
            }
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_customer_civilities_daily.route("")
class CustomerCivility(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt"}},
                    "Acheteur.Civilite": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": {"date": "$date", "Civilite": "$Acheteur.Civilite"},
                    "total": {"$sum": "$Nb"}
                }
            }
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response
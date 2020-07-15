import json
from flask import jsonify, request
from flask_restplus import Namespace, Resource
from bson.json_util import dumps
from bson.objectid import ObjectId

import config
import utilities

ns_customer_civilities = Namespace('customer/civilities', description="statistics stuff")
ns_customer_civilities_daily = Namespace('customer/civilities/daily', description="statistics stuff")


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
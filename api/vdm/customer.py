import json
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_customer_civilities = Namespace('customer/civilities', description="statistics stuff")
ns_customer_civilities_daily = Namespace('customer/civilities/daily', description="statistics stuff")
ns_spectator_civilities = Namespace('spectator/civilities', description="Histo split man / wooman")
ns_spectator_civilities_daily = Namespace('spectator/civilities/daily', description="Daily split man / wooman")

ns_customer_version = Namespace('version', description="Histo split VR / Not VR")
ns_customer_version_daily = Namespace('version/daily', description="Daily split VR / Not VR")
ns_spectator_version = Namespace('spectator/version', description="Histo split VR / Not VR")
ns_spectator_version_daily = Namespace('spectator/version/daily', description="Daily split VR / Not VR")

ns_customerBookingsHours = Namespace('customer/hours', description="dispatch customer by hours")
ns_spectatorsBookingsHours = Namespace('spectators/hours', description="dispatch Spectators by hours")

ns_customer_game_hours = Namespace('customer/game/hours', description="dispatch customer by Games hours")
ns_spectatorGamehours = Namespace('spectator/game/hours', description="dispatch Spectators by Games hours")

ns_customerSplitAge = Namespace('customerhours', description="dispatch customer by hours")
ns_spectatorSplitAge = Namespace('spectator/hours', description="dispatch Spectators by hours")


@ns_customer_civilities.route("/")
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
class CustomerCivilityDay(Resource):
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


@ns_spectator_civilities.route("/")
class SpectatorCivility(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Reservation.Spectateur.Civilite": 1,
                }
            },
            {
                "$group":
                {
                    "_id": "$Reservation.Spectateur.Civilite",
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$limit": 3}
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_spectator_civilities_daily.route("")
class SpectatorCivilityDaily(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt"}},
                    "Reservation.Spectateur.Civilite": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": {"date": "$date", "Civilite": "$Reservation.Spectateur.Civilite"},
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


@ns_customer_version.route("/")
class CustomerVersion(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Game.VR": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": "$Game.VR",
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


@ns_customer_version_daily.route("")
class CustomerVersionDaily(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt"}},
                    "Game.VR": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": {"date": "$date", "Civilite": "$Game.VR"},
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


@ns_spectator_version.route("/")
class SpectatorVersion(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Game.VR": 1,
                    "Nb": {"$size": "$Reservation"} 
                }
            },
            {
                "$group":
                {
                    "_id": "$Game.VR",
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


@ns_spectator_version_daily.route("")
class SpectatorVersionDaily(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt"}},
                    "Game.VR": 1,
                    "Nb": {"$size": "$Reservation"} 
                }
            },
            {
                "$group":
                {
                    "_id": {"date": "$date", "Civilite": "$Game.VR"},
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


@ns_customer_game_hours.route("/")
class CustomerBookingHours(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Game.Horaire": 1,
                    "Nb": {"$sum": 1} 
                }
            },
            {
                "$group":
                {
                    "_id": "$Game.Horaire",
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






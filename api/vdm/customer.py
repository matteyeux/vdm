import json
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_customer_civilities = Namespace('customer/civilities', description="statistics stuff") #OK
ns_customer_civilities_daily = Namespace('customer/civilities/daily', description="statistics stuff") #OK
ns_spectator_civilities = Namespace('spectator/civilities', description="Histo split man / wooman") #TODO
ns_spectator_civilities_daily = Namespace('spectator/civilities/daily', description="Daily split man / wooman") #TODO

ns_customer_version = Namespace('customer/version', description="Histo split VR / Not VR") #OK
ns_customer_version_daily = Namespace('customer/version/daily', description="Daily split VR / Not VR") #OK
ns_spectator_version = Namespace('spectator/version', description="Histo split VR / Not VR") #OK
ns_spectator_version_daily = Namespace('spectator/version/daily', description="Daily split VR / Not VR") #OK

ns_customer_bookings_hours = Namespace('customer/bookings/hours', description="dispatch customer by hours") #OK
ns_spectator_bookings_hours = Namespace('spectator/bookings/hours', description="dispatch Spectators by hours") #OK

ns_customer_game_hours = Namespace('customer/game/hours', description="dispatch customer by Games hours") #OK
ns_spectator_game_hours = Namespace('spectator/game/hours', description="dispatch Spectators by Games hours") #OK

ns_customer_split_age = Namespace('customer/age', description="dispatch customer by age") #OK
ns_spectator_split_age = Namespace('spectator/age', description="dispatch Spectators by age") #TODO


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
            },
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
            },
            {"$sort": {"_id": 1}},
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
                    "_id": 1,
                    "Reservation.Spectateur.Civilite": 1,

                }
            },
            # {"$limit": 10}
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
                }
            },
            # {
            #     "$group":
            #     {
            #         "_id": {"date": "$date", "Civilite": "$Reservation.Spectateur.Civilite"},
            #         "total": {"$sum": "$Nb"}
            #     }
            # },
            # {"$limit": 10}
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
                    "_id": {"date": "$date", "VR": "$Game.VR"},
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$sort": {"_id": 1}},
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
                    "_id": {"date": "$date", "VR": "$Game.VR"},
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$sort": {"_id": 1}},
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_customer_bookings_hours.route("/")
class CustomerBookingsHours(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "hours": {"$dateToString": {"format": "%H", "date": "$CreatedAt"}},
                    "Nb": {"$sum": 1}
                }
            },
            {
                "$group":
                {
                    "_id": {"hours": "$hours"},
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$sort": {"_id": 1}},
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_spectator_bookings_hours.route("/")
class SpectatorBookingsHours(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "hours": {"$dateToString": {"format": "%H", "date": "$CreatedAt"}},
                    "Nb": {"$size": "$Reservation"}
                }
            },
            {
                "$group":
                {
                    "_id": {"hours": "$hours"},
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$sort": {"_id": 1}},
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
class CustomerGameHours(Resource):
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
            },
            {"$sort": {"_id": 1}},
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_spectator_game_hours.route("/")
class SpectatorGameHours(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Game.Horaire": 1,
                    "Nb": {"$size": "$Reservation"}
                }
            },
            {
                "$group":
                {
                    "_id": "$Game.Horaire",
                    "total": {"$sum": "$Nb"}
                }
            },
            {"$sort": {"_id": 1}},
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_customer_split_age.route("/")
class CustomerSplitAge(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Acheteur.Age": 1,
                    "Nb": {"$sum": 1}
                }
            },
            # {"$limit": 3},
            {
                "$group": {
                    "_id": '',
                    "[0-18[": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$and": [
                                        {"$gte": ["$Acheteur.Age", 0]},
                                        {"$lt": ["$Acheteur.Age", 18]},
                                    ]
                                }, 
                                1, 
                                0
                            ],
                        }
                    },
                    "[18-25[": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$and": [
                                        {"$gte": ["$Acheteur.Age", 18]},
                                        {"$lt": ["$Acheteur.Age", 25]},
                                    ]
                                }, 
                                1, 
                                0
                            ],
                        }
                    },
                    "[25-39]": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$and": [
                                        {"$gte": ["$Acheteur.Age", 25]},
                                        {"$lte": ["$Acheteur.Age", 39]},
                                    ]
                                }, 
                                1, 
                                0
                            ],
                        }
                    },
                    "[40-54]": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$and": [
                                        {"$gte": ["$Acheteur.Age", 40]},
                                        {"$lte": ["$Acheteur.Age", 54]},
                                    ]
                                }, 
                                1, 
                                0
                            ],
                        }
                    },
                    "[55 et plus": {
                        "$sum": {
                            "$cond": [
                                {
                                    "$and": [
                                        {"$gte": ["$Acheteur.Age", 55]},
                                    ]
                                }, 
                                1, 
                                0
                            ],
                        }
                    },
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


@ns_spectator_split_age.route("/")
class SpectatorSplitAge(Resource):
    def get(self):  
        """Get reservation by ID."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project":
                {
                    "Reservation.Spectateur.Age": 1,
                    "Nb": {"$sum": 1}
                }
            },
        ])

        data = []
        for reservation in cursor:
            res_str =json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response

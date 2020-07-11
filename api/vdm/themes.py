import json
from flask import jsonify
from bson.json_util import dumps
from flask_restplus import Namespace, Resource
import config

ns_caThemeDays = Namespace('caThemeDays', description="CA per theme and days")
ns_cadThemeFirst = Namespace('cadThemeFirst',
                             description="CAD per First theme")
ns_cadThemeSecond = Namespace('cadThemeSecond',
                              description="CAD per Second theme")

ns_ptRoomThemesF = Namespace('ptRoomThemesF',
                             description="Points distributed per \
                             rooms and themes First")
ns_ptRoomThemesS = Namespace('ptRoomThemesS',
                             description="Points distributed per \
                             rooms and themes Second")


@ns_caThemeDays.route("/")
class CaThemeDays(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "date": {"$dateToString": {"format": "%d/%m/%Y",
                                               "date": "$CreatedAt"}},
                    "Game.theme_pricipal": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"date": "$date", "first_theme":
                            "$Game.theme_pricipal", "second_theme":
                            "$Game.theme_secondaire"},
                    "CA": {"$sum": "$CA"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            },
            {
                "$group": {
                    "_id": "$_id.date",
                    "Themes": {"$push": {
                        "First_theme": "$_id.first_theme",
                        "Second_theme": "$_id.second_theme",
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


@ns_cadThemeFirst.route("/")
class CadThemeFirst(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.theme_pricipal": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"ThemeF": "$Game.theme_pricipal"},
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


@ns_cadThemeSecond.route("/")
class CadThemeSecond(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"ThemeS": "$Game.theme_secondaire"},
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


@ns_ptRoomThemesF.route("/")
class PtRoomThemesF(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.Nom": 1,
                    "Game.theme_pricipal": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"Salle": "$Game.Nom",
                            "ThemeF": "$Game.theme_pricipal"},
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


@ns_ptRoomThemesS.route("/")
class PtRoomThemesS(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.Nom": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size": "$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"Salle": "$Game.Nom", "ThemeS":
                            "$Game.theme_secondaire"},
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

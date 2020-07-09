from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
from flask_cors import CORS
from bson import Binary, Code
from bson.objectid import ObjectId
from bson.json_util import loads, dumps
from datetime import datetime
import json
import config
import utilities

app = Flask(__name__)
api = Api(app=app, version='0.1.0', title='VDM Api',
          description='Awesome API', validate=True)

CORS(app, resources={r"": {"origins": "*"}})

ns_root = api.namespace('/', description="root")
ns_reservation = api.namespace('reservation', description="reservation stuff")
ns_reservations = api.namespace('reservations', description="reservations stuff")
ns_bookingList = api.namespace('bookingList', description="booking list stuff")
ns_incrementBookingList = api.namespace('incrementBookingList', description="incremental booking list stuff")
ns_kpiBookingList = api.namespace('kpiBookingList', description="kpi of page booking list")
ns_caDays = api.namespace('caDays', description="CA per day")
ns_caSplitOldNew = api.namespace('caSplitOldNew', description="CA per split customer Old / New")
ns_caRoomDays = api.namespace('caRoomDays', description="CA per rooms and days")
ns_cadRoom = api.namespace('cadRoom', description="CAD per rooms")
ns_caThemeDays = api.namespace('caThemeDays', description="CA per theme and days")

ns_cadThemeFirst = api.namespace('cadThemeFirst', description="CAD per First theme")
ns_cadThemeSecond = api.namespace('cadThemeSecond', description="CAD per Second theme")

ns_ptThemeDays = api.namespace('ptThemeDays', description="Points per theme and days")
ns_ptdTheme = api.namespace('ptdTheme', description="Points to date per theme")

ns_ptRoomThemesF = api.namespace('ptRoomThemesF', description="Points distributed per rooms and themes First")
ns_ptRoomThemesS = api.namespace('ptRoomThemesS', description="Points distributed per rooms and themes Second")


@ns_root.route('/')
class default_root(Resource):
    def get(self):
        """Index."""
        return "Welcome to VDM escape game\n"


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
        cursor = vdm_database.booking.find({},{'_id':0}).sort("_id", -1).limit(100)
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
            {"$project":
                {
                    "_id": 1,
                    "Acheteur.Nom":1,
                    "Acheteur.Prenom":1,
                    "NbSpectateur":{"$size":"$Reservation"},
                    "Game.Nom":1,
                    "Game.Jour":1,
                    "TotalPrice":{"$sum":"$Reservation.prix"}
                }
            },
            { "$sort" : {"_id": 1}},
            # { "$limit" : 40 }
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
            {"$project":
                {
                    "_id": 1,
                    "Acheteur.Nom":1,
                    "Acheteur.Prenom":1,
                    "NbSpectateur":{"$size":"$Reservation"},
                    "Game.Nom":1,
                    "Game.Jour":1,
                    "TotalPrice":{"$sum":"$Reservation.prix"}
                }
            },
            # {"$match": { "_id": { "$gt": ObjectId("5ef8ce087d4c386ea0025db0")}}},
            {"$match": { "_id": { "$gt": ObjectId(lastId)}}},
            # { "$limit" : 2 }
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_kpiBookingList.route("/")
class KpiBookingList(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {"$project":
                {
                    "_id": 1,
                    "NbSpectateur":{"$size":"$Reservation"},
                    "TotalPrice":{"$sum":"$Reservation.prix"}
                },
            },
            # {"$match": { "CreatedAt": { "$gte": datetime(2019, 7, 6, 0, 0)}}},
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_caDays.route("/")
class CADays(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt" }},
                    "CA": {"$sum": "$Reservation.prix"}
                }
            },
            {
                "$group": {
                    "_id": "$date",
                    "CA": {"$sum": "$CA"}
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

# TODO 
@ns_caSplitOldNew.route("/")
class CaSplitOldNew(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
        ])
        data = []
        for reservation in cursor:
            res_str = json.loads(dumps(reservation))
            data.append(res_str)

        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response


@ns_caRoomDays.route("/")
class CaRoomDays(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt" }},
                    "Game.Nom": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
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
                "$group":{
                    "_id": "$_id.date",
                    "Rooms": { "$push": {
                        "Room": "$_id.Room",
                        "CA": "$CA",
                        "Nb_Spec": "$Nb_Spec",
                    }}
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
                    "Nb_Spec": {"$size":"$Reservation"}
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


@ns_caThemeDays.route("/")
class CaThemeDays(Resource):
    def get(self):
        """Get bookinglist information."""
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt" }},
                    "Game.theme_pricipal": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"date": "$date", "first_theme": "$Game.theme_pricipal", "second_theme": "$Game.theme_secondaire"},
                    "CA": {"$sum": "$CA"},
                    "Nb_Spec": {"$sum": "$Nb_Spec"}
                }
            },
            {
                "$group":{
                    "_id": "$_id.date",
                    "Themes": { "$push": {
                        "First_theme": "$_id.first_theme",
                        "Second_theme": "$_id.second_theme",
                        "CA": "$CA",
                        "Nb_Spec": "$Nb_Spec",
                    }}
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


@ns_cadThemeFirst.route("/")
class CadThemeFirst(Resource):
    def get(self):
        """Get bookinglist information."""
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.theme_pricipal": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
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
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
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


# #################################
# TODO
# #################################
@ns_ptThemeDays.route("/")
class PtThemeDays(Resource):
    def get(self):
        """Get bookinglist information."""
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "date": {"$dateToString": {"format": "%d/%m/%Y", "date": "$CreatedAt" }},
                    "Game.theme_pricipal": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"date": "$date", "first_theme": "$Game.theme_pricipal", "second_theme": "$Game.theme_secondaire"},
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

# #################################
# TODO
# #################################
@ns_ptdTheme.route("/")
class PtdTheme(Resource):
    def get(self):
        """Get bookinglist information."""
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.theme_pricipal": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"first_theme": "$Game.theme_pricipal", "second_theme": "$Game.theme_secondaire"},
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


@ns_ptRoomThemesF.route("/")
class PtRoomThemesF(Resource):
    def get(self):
        """Get bookinglist information."""
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.Nom": 1,
                    "Game.theme_pricipal": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"Salle": "$Game.Nom", "ThemeF": "$Game.theme_pricipal"},
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
        today = datetime.today().date().isoformat()
        print(today)
        vdm_database = config.setup_mongo()
        cursor = vdm_database.booking.aggregate([
            {
                "$project": {
                    "_id": 0,
                    "Game.Nom": 1,
                    "Game.theme_secondaire": 1,
                    "CA": {"$sum": "$Reservation.prix"},
                    "Nb_Spec": {"$size":"$Reservation"}
                }
            },
            {
                "$group": {
                    "_id": {"Salle": "$Game.Nom", "ThemeS": "$Game.theme_secondaire"},
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

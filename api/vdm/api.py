from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS

from booking import (ns_reservations, ns_reservation,
                     ns_bookingList, ns_incrementBookingList)
from daily import ns_caDays, ns_nbBookingDays, ns_nbSpectDays
from kpi import ns_dailyKPI, ns_kpi
from rooms import ns_caRoomDays, ns_cadRoom
from themes import (ns_caThemeDays, ns_cadThemeFirst,
                    ns_cadThemeSecond, ns_ptRoomThemesF, ns_ptRoomThemesS)
from extract import ns_extractKPIDaily, ns_extractKPIHisto 

app = Flask(__name__)
api = Api(app=app, version='0.1.0', title='VDM Api',
          description='Awesome API', validate=True)

CORS(app, resources={r"": {"origins": "*"}})

ns_root = api.namespace('/', description="root")

api.add_namespace(ns_reservations)
api.add_namespace(ns_reservation)
api.add_namespace(ns_bookingList)
api.add_namespace(ns_incrementBookingList)

api.add_namespace(ns_caDays)
api.add_namespace(ns_nbBookingDays)
api.add_namespace(ns_nbSpectDays)

api.add_namespace(ns_dailyKPI)
api.add_namespace(ns_kpi)

api.add_namespace(ns_caRoomDays)
api.add_namespace(ns_cadRoom)

api.add_namespace(ns_caThemeDays)
api.add_namespace(ns_cadThemeFirst)
api.add_namespace(ns_cadThemeSecond)
api.add_namespace(ns_ptRoomThemesF)
api.add_namespace(ns_ptRoomThemesS)

api.add_namespace(ns_extractKPIDaily)
api.add_namespace(ns_extractKPIHisto)


@ns_root.route('/')
class default_root(Resource):
    def get(self):
        """Index."""
        return "Welcome to VDM escape game\n"

from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS

from booking import (ns_reservations, ns_reservation,
                     ns_bookingList, ns_bookingListDay,
                      ns_incrementBookingList, ns_bookingDetail,
                      ns_bookingListExtract, ns_firstDate,
                      ns_lastDate)
from daily import ns_caDays, ns_nbBookingDays, ns_nbSpectDays
from kpi import ns_dailyKPI, ns_kpi
from rooms import ns_caRoomDays, ns_cadRoom
from themes import (ns_caThemeDays, ns_cadThemeFirst,
                    ns_cadThemeSecond, ns_ptRoomThemesF, ns_ptRoomThemesS)
from extract import ns_extractKPIDaily, ns_extractKPIHisto 
from customer import (ns_customer_civilities, ns_customer_civilities_daily,
                    ns_spectator_civilities, ns_spectator_civilities_daily,
                    ns_customer_version, ns_customer_version_daily,
                    ns_spectator_version, ns_spectator_version_daily,
                    ns_customer_bookings_hours, ns_spectator_bookings_hours,                
                    ns_customer_game_hours, ns_spectator_game_hours,
                    ns_customer_split_age, ns_spectator_split_age                    
                    )

app = Flask(__name__)
api = Api(app=app, version='0.1.0', title='VDM Api',
          description='Awesome API', validate=True)

CORS(app, resources={r"": {"origins": "*"}})

ns_root = api.namespace('/', description="root")

api.add_namespace(ns_reservations)
api.add_namespace(ns_reservation)
api.add_namespace(ns_bookingList)
api.add_namespace(ns_bookingListDay)
api.add_namespace(ns_incrementBookingList)
api.add_namespace(ns_bookingDetail)
api.add_namespace(ns_bookingListExtract)
api.add_namespace(ns_firstDate)
api.add_namespace(ns_lastDate)


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

api.add_namespace(ns_customer_civilities)
api.add_namespace(ns_customer_civilities_daily)
api.add_namespace(ns_spectator_civilities)
api.add_namespace(ns_spectator_civilities_daily)

api.add_namespace(ns_customer_version)
api.add_namespace(ns_customer_version_daily)
api.add_namespace(ns_spectator_version)
api.add_namespace(ns_spectator_version_daily)

api.add_namespace(ns_customer_bookings_hours)
api.add_namespace(ns_spectator_bookings_hours)

api.add_namespace(ns_customer_game_hours)
api.add_namespace(ns_spectator_game_hours)

api.add_namespace(ns_customer_split_age)
api.add_namespace(ns_spectator_split_age)


@ns_root.route('/')
class default_root(Resource):
    def get(self):
        """Index."""
        return "Welcome to VDM escape game\n"

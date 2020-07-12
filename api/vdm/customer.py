import json
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restplus import Namespace, Resource
from datetime import datetime

import config

ns_buyerSex = Namespace('buyerSex', description="Histo split man / wooman")
ns_buyerSexDaily = Namespace('buyerSexDaily', description="Daily split man / wooman")
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
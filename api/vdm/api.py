from flask import Flask, jsonify, request
import json
import config


app = Flask(__name__)


@app.route('/')
def index():
    """Index."""
    return "Welcome to VDM escape game\n"


def handle_prices(data: dict) -> dict:
    """Set price according to rate."""
    for reservation in data['Reservation']:
        if reservation['Tarif'] == "Plein tarif":
            price = 9.40
        elif reservation['Tarif'] == "Tarif reduit":
            price = 7.40
        elif reservation['Tarif'] == "Senior":
            price = 6.80
        elif reservation['Tarif'] == "Tarif étudiant":
            price = 6.80
        else:
            price = None
        reservation['prix'] = price
    return data


@app.route('/register', methods=["POST"])
def register_data():
    """Register booking data."""
    mongodb_col = config.setup_mongo()
    data = handle_prices(request.json)
    print(json.dumps(data, indent=4))

    mongodb_col.insert_one(request.json)
    return jsonify({"message": "created"}), 201


@app.route('/data', methods=["GET"])
def get_booking_data():
    """Return booking data."""
    mongo_col = config.setup_mongo()

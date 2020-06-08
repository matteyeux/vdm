from flask import Flask, jsonify, request
import config
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to VDM escape game\n"


@app.route('/register', methods=["POST"])
def register_data():
    mongodb_col = config.setup_mongo()
    mongodb_col.insert_one(request.json)
    return jsonify({"message": "created"}), 201

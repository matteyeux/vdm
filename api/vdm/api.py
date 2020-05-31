from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to VDM escape game\n"

@app.route('/register', methods=["POST"])
def register_data():
    print(request.json)
    return jsonify({"message" : "created"}), 201

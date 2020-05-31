from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to VDM escape game\n"

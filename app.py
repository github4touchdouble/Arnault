from flask import Flask, jsonify, request
from datetime import datetime
from handlers import chat
app = Flask(__name__)

@app.route("/api")
def hello_world():
    data = {
        "response": f"Hello, this is the Arnault API v0.1 current date and time is {datetime.now()}."
    }
    return jsonify(data)

@app.route("/api", methods=["POST"])
def ask_albert():
    # check if request is in JSON format
    if not request.is_json:
        return jsonify({"error": "Invalid request format"}), 400

    # parse request JSON data
    data = request.get_json()
    # check if required fields are present in request data
    if "input" not in data:
        return jsonify({"error": "Missing required field 'input'"}), 400

    #ask arnault
    input_text = data["input"]
    response = chat(input_text)

    return jsonify({"response": response}), 200

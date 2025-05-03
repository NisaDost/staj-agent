#validate_path.py

import os
from flask import Flask, request, jsonify
from threading import Thread
from utilities.logger import logger

def validate_path(path):
    isValid = False
    # Check if the path exists
    if not os.path.exists(path):
        logger.error(f"[INVALID] Path does not exist: {path}")
        isValid = False
        return isValid
    
    # Check if it's a directory
    if not os.path.isdir(path):
        logger.error(f"[INVALID] Path is not a valid directory: {path}")
        isValid = False
        return isValid

    # If it's a valid directory
    logger.info(f"[VALID] Path is valid directory: {path}")
    isValid = True
    return isValid


app = Flask(__name__)

@app.route('/check-path', methods=['POST'])
def check_path():
    data = request.get_json()
    path = data.get("path")

    logger.info(f"Received path validation request: {path}")

    if not path or not isinstance(path, str):
        return jsonify({"valid": False, "error": "Missing or invalid path"}), 400

    if not validate_path(path):
        return jsonify({"valid": False}), 200

    return jsonify({"valid": True}), 200

def run_agent_server():
    logger.info("Starting local Flask server for agent path validation...")
    app.run(host='0.0.0.0', port=5005, debug=False, use_reloader=False)

def start_flask_server():
    t = Thread(target=run_agent_server)
    t.daemon = True
    t.start()
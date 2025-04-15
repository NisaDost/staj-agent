#agent_api.py

from flask import Flask, request, jsonify
import os
from utils import is_valid_directory_path
from threading import Thread
from utils import logger

app = Flask(__name__)

@app.route('/check-path', methods=['POST'])
def check_path():
    data = request.get_json()
    path = data.get("path")

    logger.info(f"🧪 Received path validation request: {path}")

    if not path or not isinstance(path, str):
        return jsonify({"valid": False, "error": "Missing or invalid path"}), 400

    if not is_valid_directory_path(path):
        return jsonify({"valid": False}), 200

    return jsonify({"valid": True}), 200

def run_agent_server():
    logger.info("🛰️ Starting local Flask server for agent path validation...")
    app.run(host='0.0.0.0', port=5005, debug=False, use_reloader=False)

def start_agent_http_server_in_background():
    t = Thread(target=run_agent_server)
    t.daemon = True
    t.start()

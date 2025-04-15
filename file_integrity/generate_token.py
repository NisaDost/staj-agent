#generate_token.py

import requests
from config import BACKEND_URL
from utils import logger

def generate_agent_instance(agent_name):
    url = f"{BACKEND_URL}/agent/generateToken"
    payload = {"agentName": agent_name}
    headers = {"Content-Type": "application/json"}
    try:
        # logger.info("Creating agent instance by calling %s", url)

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        # logger.info("Agent instance created: %s", data)
        
        return data  # data contains agentId, token, message. No need to print.
    except requests.RequestException as e:
        logger.error("Failed to create agent instance: %s", str(e))
        return None

#activation.py

import requests
from config import BACKEND_URL
from utils import logger

def activate_agent(user_token):
    url = f"{BACKEND_URL}/agent/activate"
    payload = {"activationToken": user_token}
    headers = {"Content-Type": "application/json"}
    try:
        #logger.info("Sending activation request to %s", url)
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        #logger.info("Activation successful: %s", data)
        return data 
    except requests.RequestException as e:
        logger.error("Activation failed. " + str(e))
        return None

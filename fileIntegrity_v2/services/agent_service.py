#agent_service.py

import string
import secrets
import requests
from config import BACKEND_URL
from utilities.logger import logger, setup_log_dir

def generate_agent_name():
    #Generates a random 12-character agent name.
    characters = string.ascii_letters + string.digits
    agent_name= "agent-" + ''.join(secrets.choice(characters) for _ in range(6))
    return agent_name

def create_agent():
    agent_name = generate_agent_name()
    setup_log_dir(agent_name)  # Set up logging directory for the agent

    url = f"{BACKEND_URL}/agent/generateToken"
    payload = {"agentName": agent_name}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        return data, agent_name  # data contains agentId, token, message. No need to print.
    except requests.RequestException as e:
        logger.error("Failed to create agent instance: %s", str(e))
        return None

def activate_agent(user_token):
    url = f"{BACKEND_URL}/agent/activate"
    payload = {"activationToken": user_token}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data 
    except requests.RequestException as e:
        logger.error("Activation failed. " + str(e))
        return None
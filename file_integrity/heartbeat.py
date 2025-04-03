import requests
import time
from config import BACKEND_URL, HEARTBEAT_INTERVAL
from utils import logger

def send_heartbeat(agent_id):
    heartbeat_url = f"{BACKEND_URL}/api/v1/agent/heartbeat"
    payload = {
        "agentId": agent_id,
        "timestamp": int(time.time()),
        "status": "active",
        "version": "1.0"
    }
    headers = {"Content-Type": "application/json"}

    try:
        logger.info("Sending heartbeat to %s", heartbeat_url)
        response = requests.post(heartbeat_url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info("Heartbeat response received: %s", data)
        return data
    except requests.RequestException as e:
        logger.error("Heartbeat failed: %s", str(e))
        return None

def start_heartbeat_loop(agent_id):
    """
    Starts the heartbeat loop that sends heartbeats at regular intervals.
    """
    global HEARTBEAT_INTERVAL  # ✅ Declare it as global before modifying
    
    while True:
        response = send_heartbeat(agent_id)
        
        if response and "config" in response:
            new_interval = response["config"].get("updateInterval")
            
            if new_interval and new_interval != HEARTBEAT_INTERVAL:
                logger.info("Updating heartbeat interval to %s seconds", new_interval)
                HEARTBEAT_INTERVAL = new_interval  # ✅ Now modifying the global variable
        
        time.sleep(HEARTBEAT_INTERVAL)

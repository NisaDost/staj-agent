import requests
import time
from config import BACKEND_URL, AGENT_ID, HEARTBEAT_INTERVAL
from utils import logger

def send_heartbeat():
    """
    Sends a heartbeat message to the backend.
    
    Returns:
        dict: The backend's response if successful, otherwise None.
    """
    heartbeat_url = f"{BACKEND_URL}/api/v1/agent/heartbeat"
    payload = {
        "agentId": AGENT_ID,
        "timestamp": int(time.time()),
        "status": "active",
        "version": "1.0"
    }
    headers = {"Content-Type": "application/json"}

    try:
        logger.info("Sending heartbeat to %s with payload: %s", heartbeat_url, payload)
        # For now, since the endpoint is not implemented, we simulate a successful response.
        # Uncomment the following lines if the backend endpoint is available:

        # response = requests.post(heartbeat_url, json=payload, headers=headers)
        # response.raise_for_status()
        # data = response.json()
        # logger.info("Heartbeat response: %s", data)
        # return data
        
        # Simulated dummy response:
        dummy_response = {
            "directories": ["/path/to/monitor"],
            "config": {"updateInterval": HEARTBEAT_INTERVAL}
        }
        logger.info("Dummy heartbeat response: %s", dummy_response)
        return dummy_response
    except requests.RequestException as e:
        logger.error("Heartbeat failed: %s", str(e))
        return None
    
    
import requests
from config import BACKEND_URL, ACTIVATION_TOKEN
from utils import logger

# def activate_agent():
#     """
#     Sends an activation request to the backend using the ACTIVATION_TOKEN.
    
#     Returns:
#         dict: Activation data from the backend if successful.
#         None: If activation fails.
#     """

#     activate_url = f"{BACKEND_URL}/api/v1/agent/activate"
#     payload = {"activationToken": ACTIVATION_TOKEN}
#     headers = {"Content-Type": "application/json"}

#     try:
#         logger.info("Sending activation request to %s", activate_url)
#         response = requests.post(activate_url, json=payload, headers=headers)
#         response.raise_for_status()
#         data = response.json()
#         logger.info("Activation successfull. Data: %s", data)
#         return data
#     except requests.RequestException as e:
#         logger.error("Activation failed: %s", str(e))
#         return None
    
def dummy_activate_agent():
    """
    Dummy activation function.
    
    Returns:
        dict: Dummy activation data.
    """
    # Simulate a delay as if communicating with backend.
    logger.info("Simulating agent activation with token.")
    dummy_response = {
        "agentId": "agent-001",
        "config": {
            "directories": ["/path/to/monitor"],
            "heartbeatInterval": 5
        },
        "message": "Activation successful"
    }
    logger.info("Activation dummy response: %s", dummy_response)
    return dummy_response
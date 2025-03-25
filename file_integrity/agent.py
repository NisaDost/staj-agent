from config import BACKEND_URL, AGENT_ID, ACTIVATION_TOKEN, HEARTBEAT_INTERVAL
from utils import logger
import time
#from activation import activate_agent
from activation import dummy_activate_agent
from heartbeat import send_heartbeat

def main():
    logger.info("Starting FileIntegrity agent %s", AGENT_ID)

    activation_info = dummy_activate_agent() # to be replaced with activate_agent()

    if activation_info is None:
        logger.error("Failed to activate agent %s. Exiting.", AGENT_ID)
        return
    
    logger.info("Agent activated successfully with response: %s", activation_info)

    while True:
        heartbeat_response = send_heartbeat()

        if heartbeat_response:
            logger.info("Heartbeat received configuration: %s", heartbeat_response)
        else:
            logger.error("Heartbeat did not receive a valid response.")
        time.sleep(HEARTBEAT_INTERVAL)


#Initializer
if __name__ == "__main__":
    main()
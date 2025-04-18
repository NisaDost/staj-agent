#agent.py
import time
from utils import logger, AGENT_NAME
from generate_token import generate_agent_instance
from activation import activate_agent
from heartbeat import start_heartbeat_and_monitoring
from agent_api import start_agent_http_server_in_background

def main():
    # Start local HTTP server for path validation
    start_agent_http_server_in_background()

    # Create agent instance
    instance_info = generate_agent_instance(AGENT_NAME)
    if instance_info is None:
        logger.error("Failed to create agent instance. Exiting.")
        return

    agent_id = instance_info.get("agentId")
    if not agent_id:
        logger.error("Agent ID not found. Exiting.")
        return


    # Activation loop
    time.sleep(1)  # Wait for a moment before starting flask server
    logger.info("Starting FileIntegrity Agent CLI for agent %s with ID: %s", AGENT_NAME, agent_id)
    activation_info = None
    while activation_info is None:
        try:
            
            user_token = input("Enter the activation token: ").strip()
            activation_info = activate_agent(user_token)
            if activation_info is None:
                logger.warning("Invalid activation token. Please try again.\n")
        except KeyboardInterrupt:
            logger.info("Exiting activation process.")
            return
    logger.info("Activation successful!")

    # Start heartbeat and monitoring loop
    start_heartbeat_and_monitoring(agent_id)

if __name__ == "__main__":
    main()

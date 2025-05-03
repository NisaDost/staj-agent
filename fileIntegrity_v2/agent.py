#agent.py
import time
from utilities.logger import logger
from services.agent_service import create_agent, activate_agent
from services.path_service import start_flask_server
from services.heartbeat_service import start_heartbeat_service

def main():
    # Start local HTTP server for path validation
    start_flask_server()

    # Create agent instance
    try:
        result = create_agent()
        if result is None:
            logger.error("Failed to create agent instance. Exiting.")
            return

        response_data, agent_name = result
        agent_id = response_data["agentId"]

    except Exception as e:
        logger.error("Error connecting to server: %s, Exiting.", str(e))
        return


    # Activation loop
    time.sleep(1)  # Wait for a moment before starting flask server

    logger.info("Starting FileIntegrity Agent CLI for agent #%s - %s.",agent_id, agent_name)
    activation_info = None
    while activation_info is None:
        try:
            agent_token = input("Enter the activation token: ").strip()
            activation_info = activate_agent(agent_token)
            if activation_info is None:
                logger.warning("Invalid activation token. Please try again.\n")
        except KeyboardInterrupt:
            logger.info("Exiting activation process.")
            return
    logger.info("Activation successful!")

    # Start heartbeat and monitoring loop
    start_heartbeat_service(agent_id)

if __name__ == "__main__":
    main()

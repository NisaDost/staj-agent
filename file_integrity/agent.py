import time
import secrets
import string
from config import HEARTBEAT_INTERVAL
from utils import logger
from generate_token import generate_agent_instance
from activation import activate_agent

def generate_agent_name():
    """Generates a random 12-character agent name."""
    characters = string.ascii_letters + string.digits
    return "agent-" + ''.join(secrets.choice(characters) for _ in range(6))  # 6 random chars

def main():
    user_agent_name = generate_agent_name()
    logger.info("Starting FileIntegrity Agent CLI for agent: %s", user_agent_name)
    
    #Create agent instance by calling the generate token endpoint.
    instance_info = generate_agent_instance(user_agent_name)
    if instance_info is None:
        logger.error("Failed to create agent instance. Exiting.")
        return

    #Inform the user about the created instance.
    agent_id = instance_info.get("agentId")
    print(f"Agent instance created with Agent ID: {agent_id} and Name: {user_agent_name}")

    #Loop until a valid activation token is entered.
    activation_info = None
    while activation_info is None:
        user_token = input("Enter the activation token: ").strip()
        activation_info = activate_agent(user_token)
        if activation_info is None:
            print("Invalid activation token. Please try again.\n")
    
    print(f"Activation successful: {activation_info}")
    
    #Start heartbeat loop 
    while True:
        print("Heartbeat...")  # Placeholder for heartbeat functionality
        time.sleep(HEARTBEAT_INTERVAL)

if __name__ == "__main__":
    main()

#utils.py
import logging
import os
import secrets
import string
import logging
import os

def generate_agent_name():
    """Generates a random 12-character agent name."""
    characters = string.ascii_letters + string.digits
    return "agent-" + ''.join(secrets.choice(characters) for _ in range(6))

AGENT_NAME = generate_agent_name()

def setup_logger(AGENT_NAME: str):
    # Determine the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")

    # Create the logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Create a separate log file for the given agent
    log_file_path = os.path.join(log_dir, f"{AGENT_NAME}.log")

    # Initialize the logger
    logger = logging.getLogger(f"AgentLogger_{AGENT_NAME}")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is reused
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # File handler for this specific agent
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional: also log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger(AGENT_NAME)

def is_valid_directory_path(path):
    
    # Check if the path exists
    if not os.path.exists(path):
        logger.error(f"[INVALID] Path does not exist: {path}")
        return False
    
    # Check if it's a directory
    if not os.path.isdir(path):
        logger.error(f"[INVALID] Path is not a valid directory: {path}")
        return False

    # If it's a valid directory
    logger.info(f"[VALID] Path is valid directory: {path}")
    return True

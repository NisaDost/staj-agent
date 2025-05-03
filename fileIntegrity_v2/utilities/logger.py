# logger.py

import os
import logging

def logger_config():
    """
    Logging format and config — only console.
    """
    logger = logging.getLogger("AgentLogger")
    logger.setLevel(logging.INFO)

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

logger = logger_config()

def setup_log_dir(agent_name: str, logger_name="AgentLogger"):
    """
    Adds file handler to logger.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, f"{agent_name}.log")
    logger = logging.getLogger(logger_name)

    if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return log_file_path

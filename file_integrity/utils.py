#utils.py
import logging
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger("FileIntegrityAgent")

logger = setup_logger()

def is_valid_directory_path(path):
    logger.info(f"Validating path: {path}")
    
    # Check if the path exists
    if not os.path.exists(path):
        logger.error(f"❌ Path does not exist: {path}")
        return False
    
    # Check if it's a directory
    if not os.path.isdir(path):
        logger.error(f"❌ Path is not a directory: {path}")
        return False

    # If it's a valid directory
    logger.info(f"✅ Path is valid directory: {path}")
    return True

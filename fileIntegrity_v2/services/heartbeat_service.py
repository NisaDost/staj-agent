#heartbeat_service.py

import requests
import time
from watchdog.observers import Observer

from config import BACKEND_URL, HEARTBEAT_INTERVAL, VERSION
from utilities.monitor_file import FileChangeHandler
from services.path_service import validate_path
from utilities.logger import logger

def send_heartbeat(agent_id):
    heartbeat_url = f"{BACKEND_URL}/agent/heartbeat"
    payload = {
        "agentId": agent_id,
        "timestamp": int(time.time()),
        "status": "active",
        "version": f"{VERSION}",
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


def fetch_directories(agent_id):
    url = f"{BACKEND_URL}/directories/get?agentId={agent_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Expecting list of {"path": "/some/path"}
    except requests.RequestException as e:
        logger.error("Failed to fetch monitored directories: %s", str(e))
        return []


def start_heartbeat_service(agent_id):

    event_handler = FileChangeHandler(agent_id)
    observer = Observer()
    observer.start()
    logger.info("Directory monitoring observer started.")

    monitored_paths = set()
    path_to_watch = {}  # This will map paths to their corresponding watch objects

    try:
        while True:
            # Heartbeat
            response = send_heartbeat(agent_id)
            
            # Optional
            # if response and "config" in response:
            #     new_interval = response["config"].get("updateInterval")
            #     if new_interval and new_interval != HEARTBEAT_INTERVAL:
            #         logger.info("Updating heartbeat interval to %s seconds", new_interval)
            #         HEARTBEAT_INTERVAL = new_interval

            # Fetch updated directory list
            directories = fetch_directories(agent_id)
            current_directories = set(dir["path"] for dir in directories)

            # Add new directories to monitoring    
            new_dirs = current_directories - monitored_paths
            for path in new_dirs:
                if not validate_path(path):
                    continue
                watch = observer.schedule(event_handler, path, recursive=True)
                path_to_watch[path] = watch  # Save the watch object
                monitored_paths.add(path)
                logger.info(f"Started Watching: {path}")

            # Remove directories no longer in the list
            dirs_to_remove = monitored_paths - current_directories
            for path in dirs_to_remove:
                watch = path_to_watch.pop(path, None)  # Retrieve the watch object
                if watch:
                    observer.unschedule(watch)  # Unwatch the directory
                monitored_paths.remove(path)
                logger.info(f"Stopped watching: {path}")

            time.sleep(HEARTBEAT_INTERVAL)

    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received, stopping observer.")
        observer.stop()
    observer.join() 
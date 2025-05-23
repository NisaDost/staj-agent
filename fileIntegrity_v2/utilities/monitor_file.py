# monitor_file.py
import requests
from watchdog.events import FileSystemEventHandler
from utilities.logger import logger
from config import BACKEND_URL

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def on_created(self, event):
        logger.info(f"[CREATED] Path: {event.src_path}, is_directory={event.is_directory}")
        self.send_event_to_backend(event.src_path, "CREATED")

    def on_modified(self, event):
        logger.info(f"[MODIFIED] Path: {event.src_path}, is_directory={event.is_directory}")
        self.send_event_to_backend(event.src_path, "MODIFIED")

    def on_deleted(self, event):
        logger.info(f"[DELETED] Path: {event.src_path}, is_directory={event.is_directory}")
        self.send_event_to_backend(event.src_path, "DELETED")

    def send_event_to_backend(self, path, event_type):
        event_data = {
            "agentId": self.agent_id,
            "changes": [{"path": path, "eventType": event_type}]
        }
        logger.info(f"Sending event: {event_data}")
        try:
            response = requests.post(f"{BACKEND_URL}/events/monitor", json=event_data)
            logger.info(f"Event sent. Backend responded: {response.status_code} - {response.text}")
            response.raise_for_status()
        except requests.RequestException:
            logger.exception("Failed to send event to backend")
#config.py

import os

# Backend URL
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8080/api/v1")

# Heartbeat interval in seconds
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", 5))

#APP Version
VERSION = os.getenv("VERSION", "1.2.0")
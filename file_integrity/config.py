import os

# Backend URL
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Agent ID
AGENT_ID = os.getenv("AGENT_ID", "agent001")

# Activation token
ACTIVATION_TOKEN = os.getenv("ACTIVATION_TOKEN", "activation_token")

# Heartbeat interval in seconds
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", 5))
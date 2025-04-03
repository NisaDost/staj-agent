import os

# Backend URL (use HTTPS in production)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8080")

# Heartbeat interval in seconds
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", 5))

# Default agent name
AGENT_NAME = os.getenv("AGENT_NAME", "agent-002")

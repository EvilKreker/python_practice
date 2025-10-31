# conftest.py
import os
import logging
import pytest
import requests
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("reqres-tests")

REQRES_BASE_URL = "https://reqres.in/api"
# In real runs you'd pull this from env/secret store; using the provided free key as default:
DEFAULT_API_KEY = "reqres-free-v1"

@pytest.fixture(scope="session")
def reqres_client():
    """
    Session-scoped fixture that:
    - SETUP: creates a requests.Session and prepares headers (simulating token acquisition)
    - YIELD: provides a small client dict to tests
    - TEARDOWN: logs/cleans up
    """
    # --- SETUP: simulate "session/token preparation" ---
    session = requests.Session()
    # Simulate obtaining/refreshing a token/API key; here we just read from env or use the provided key
    api_key = os.environ.get("REQRES_API_KEY", DEFAULT_API_KEY)

    # Common headers for authenticated calls (only used where required)
    auth_headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
        # You could add a simulated bearer token here if needed:
        # "Authorization": f"Bearer {fake_token}"
    }

    logger.info("===> [SETUP] Prepared session and auth headers at %s", datetime.utcnow().isoformat())

    client = {
        "session": session,
        "base_url": REQRES_BASE_URL,
        "auth_headers": auth_headers,
        "user_endpoint": f"{REQRES_BASE_URL}/users/2",
    }

    # Hand control to tests
    yield client

    # --- TEARDOWN: simulate cleanup/logging ---
    session.close()
    logger.info("===> [TEARDOWN] Closed session at %s", datetime.utcnow().isoformat())

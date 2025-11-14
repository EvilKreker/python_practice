# tests/api/conftest.py
import logging
from datetime import datetime
import pytest
import requests

log = logging.getLogger("reqres-tests")
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="session")
def reqres_client():
    session = requests.Session()
    base_url = "https://reqres.in/api"
    api_key = "reqres-free-v1"  # or from env if you prefer

    # ✅ Make the API key default for ALL requests (incl. GET)
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": api_key,
    })

    client = {
        "session": session,
        "base_url": base_url,
        "user_endpoint": f"{base_url}/users/2",
        # still keep explicit headers in case a test needs to override/extend
        "auth_headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": api_key,
        },
    }

    log.info("===> [SETUP] Prepared session and auth headers at %s", datetime.utcnow().isoformat())
    yield client
    session.close()
    log.info("===> [TEARDOWN] Session closed")
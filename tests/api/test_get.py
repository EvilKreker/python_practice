import pytest

def test_get_user_success(reqres_client):
    """
    GET should NOT require API key per requirement.
    Asserts 200 and key fields in the response body.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]

    resp = s.get(url, timeout=15)
    assert resp.status_code == 200, f"Unexpected status {resp.status_code}: {resp.text}"

    data = resp.json()
    assert "data" in data, "Expected 'data' key in response"
    user = data["data"]

    assert user.get("id") == 2, f"Expected id=2, got {user.get('id')}"

    for field in ("email", "first_name", "last_name", "avatar"):
        assert field in user, f"Missing '{field}' in user payload"

    assert "support" in data and "url" in data["support"], "Expected 'support.url' to exist"
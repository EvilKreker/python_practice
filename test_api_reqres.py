# test_api_reqres.py
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
    # Basic structure checks
    assert "data" in data, "Expected 'data' key in response"
    user = data["data"]
    # Content checks
    assert user.get("id") == 2, f"Expected id=2, got {user.get('id')}"
    # A couple of fields ReqRes typically returns
    for field in ("email", "first_name", "last_name", "avatar"):
        assert field in user, f"Missing '{field}' in user payload"

    # Support block often present in ReqRes
    assert "support" in data and "url" in data["support"], "Expected 'support.url' to exist"


@pytest.mark.parametrize("payload", [
    {"name": "morpheus", "job": "leader"},
    {"name": "neo", "job": "the one"},
])
def test_post_user_with_api_key(reqres_client, payload):
    """
    POST requires API key header.
    Since we're posting to /users/2 (per the requirement's endpoint structure),
    we allow typical success codes and look for echoed or creation markers.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]
    headers = reqres_client["auth_headers"]

    resp = s.post(url, json=payload, headers=headers, timeout=15)

    # Accept common "success" statuses for POST on public mocks (ReqRes usually uses 201 for /users)
    assert resp.status_code in (200, 201, 202), f"Unexpected status {resp.status_code}: {resp.text}"

    body = resp.json()
    # Meaningful assertions: name/job usually echo back on ReqRes
    for k, v in payload.items():
        assert body.get(k) == v, f"Expected echoed {k}={v}, got {body.get(k)}"

    # On creation/update, ReqRes typically returns id/createdAt or updatedAt
    assert any(k in body for k in ("id", "createdAt", "updatedAt")), "Expected an id/createdAt/updatedAt field"


def test_put_user_with_api_key(reqres_client):
    """
    PUT requires API key header.
    Assert 200-ish and presence of updatedAt; also echo of sent fields.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]
    headers = reqres_client["auth_headers"]

    payload = {"name": "trinity", "job": "operator"}
    resp = s.put(url, json=payload, headers=headers, timeout=15)

    assert resp.status_code in (200, 201), f"Unexpected status {resp.status_code}: {resp.text}"
    body = resp.json()

    for k, v in payload.items():
        assert body.get(k) == v, f"Expected echoed {k}={v}, got {body.get(k)}"

    assert "updatedAt" in body, "Expected 'updatedAt' timestamp in PUT response"


def test_delete_user_with_api_key(reqres_client):
    """
    DELETE requires API key header.
    ReqRes typically returns 204 No Content for DELETE /users/2.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]
    headers = reqres_client["auth_headers"]

    resp = s.delete(url, headers=headers, timeout=15)
    assert resp.status_code in (204, 200), f"Unexpected status {resp.status_code}: {resp.text}"

    # If 204, no body; if 200 from some gateways, body may be empty string or JSON
    content = resp.text.strip()
    assert content == "" or content == "{}" or content.startswith("{") is True or resp.status_code == 204

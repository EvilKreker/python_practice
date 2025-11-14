import pytest

@pytest.mark.parametrize("payload", [
    {"name": "morpheus", "job": "leader"},
    {"name": "neo", "job": "the one"},
])
def test_post_user_with_api_key(reqres_client, payload):
    """
    POST requires API key header.
    Asserts success status and echoed fields.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]
    headers = reqres_client["auth_headers"]

    resp = s.post(url, json=payload, headers=headers, timeout=15)
    assert resp.status_code in (200, 201, 202), f"Unexpected status {resp.status_code}: {resp.text}"

    body = resp.json()
    for k, v in payload.items():
        assert body.get(k) == v, f"Expected echoed {k}={v}, got {body.get(k)}"

    assert any(k in body for k in ("id", "createdAt", "updatedAt")), \
        "Expected an id/createdAt/updatedAt field in response"
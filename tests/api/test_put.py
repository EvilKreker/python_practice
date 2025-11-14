def test_put_user_with_api_key(reqres_client):
    """
    PUT requires API key header.
    Asserts 200-ish response and presence of updatedAt.
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
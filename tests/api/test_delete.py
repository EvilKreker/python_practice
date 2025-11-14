def test_delete_user_with_api_key(reqres_client):
    """
    DELETE requires API key header.
    Asserts 204 or 200 and verifies empty or JSON body.
    """
    s = reqres_client["session"]
    url = reqres_client["user_endpoint"]
    headers = reqres_client["auth_headers"]

    resp = s.delete(url, headers=headers, timeout=15)
    assert resp.status_code in (204, 200), f"Unexpected status {resp.status_code}: {resp.text}"

    content = resp.text.strip()
    assert content == "" or content == "{}" or content.startswith("{") or resp.status_code == 204, \
        "Unexpected DELETE response content"
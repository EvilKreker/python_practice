⸻


# REST API Tests for ReqRes Demo Service

This repository contains automated REST API tests for the [ReqRes](https://reqres.in) demo service, written in **Python** using **pytest** and the **requests** library.  
The tests validate the behavior of the `/api/users/2` endpoint with the full CRUD cycle — **GET**, **POST**, **PUT**, and **DELETE** — using a reusable fixture that simulates authenticated sessions.

---

##  Project Structure

conftest.py          ## Pytest fixture for session/token setup and teardown

test_api_reqres.py   ## Main test file (GET, POST, PUT, DELETE tests)

README.md            ## Project documentation

---

##  Requirements

- **Python:** 3.8+
- **Libraries:**
  - `pytest`
  - `requests`

Install dependencies:
```bash
pip install pytest requests


⸻

Authentication

For POST, PUT, and DELETE requests, ReqRes requires an API key:

x-api-key: reqres-free-v1

By default, the fixture uses this key automatically.
You can override it by setting an environment variable:

export REQRES_API_KEY="your-custom-key"


⸻

Fixture Overview (reqres_client)

Defined in conftest.py:
	•	Setup:
	•	Creates a requests.Session
	•	Simulates session/token preparation
	•	Injects the API key header
	•	Teardown:
	•	Closes the session
	•	Logs cleanup details

This fixture uses yield to clearly separate setup and teardown stages.

⸻

Test Cases

Method	Description	Auth Required	Key Assertions
GET	Retrieve existing user /api/users/2	----	Status 200, validate user structure (id, email, first_name, etc.)
POST	Create/update user at /api/users/2	----	Status 200/201, echo name & job, presence of id or createdAt
PUT	Update user data /api/users/2	----	Status 200/201, echo name & job, check updatedAt
DELETE	Remove user /api/users/2	----	Status 204 or 200, no response body


⸻

Running the Tests

Run all tests:

pytest -v

Run a single test file:

pytest test_api_reqres.py -v


⸻

Example Output

collected 4 items

test_api_reqres.py::test_get_user_success PASSED
test_api_reqres.py::test_post_user_with_api_key[morpheus-leader] PASSED
test_api_reqres.py::test_put_user_with_api_key PASSED
test_api_reqres.py::test_delete_user_with_api_key PASSED

All tests pass successfully against the ReqRes public API.

⸻

Notes
	•	The ReqRes service is public and stateless — changes are not persisted.
	•	Tests are designed to verify structure, responses, and status codes rather than real data persistence.
	•	This setup demonstrates:
	•	Usage of pytest fixtures
	•	API key authentication
	•	Full CRUD validation for REST APIs
	•	Proper setup/teardown handling

⸻

Optional: Continuous Integration

You can easily run these tests in GitHub Actions by adding a workflow file:

Create .github/workflows/tests.yml:

name: Run API Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pytest requests

      - name: Run tests
        run: pytest -v


⸻

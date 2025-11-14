====================================
python_practice — Automated Testing
====================================

This project contains two main practical tasks for automated testing in Python:
1) API Testing using pytest + requests
2) UI Testing using pytest + Playwright (synchronous API)

----------------------------------------
TASK 1: API TESTING (Pytest + Requests)
----------------------------------------

Description:
------------
Implements REST API tests with CRUD operations (GET, POST, PUT, DELETE)
against the public demo API: https://reqres.in/api/users/2

Purpose:
--------
To verify different HTTP methods, response codes, and payload structures
using pytest assertions and a reusable fixture (conftest.py).

Key Features:
-------------
- Each HTTP method has a separate test file.
- Session fixture (`conftest.py`) manages API key, headers, and session setup.
- Uses API key header: x-api-key: reqres-free-v1
- Validates:
  * HTTP status codes
  * Response JSON structure
  * Expected field values

Project Layout (API):
---------------------
<pre>
tests/
│
└── api/
    ├── conftest.py
    ├── test_get_user.py
    ├── test_post_user.py
    ├── test_put_user.py
    └── test_delete_user.py
</pre>


How to Run API Tests:
---------------------
1. Activate virtual environment.
2. Run the following command from the project root:

   pytest tests/api -v

To run a specific test file:

   pytest tests/api/test_post_user.py -v

Expected Results:
-----------------
- GET → 200 OK and valid user data with "id": 2
- POST → 201 Created and echoed payload (name/job)
- PUT → 200 OK with updatedAt timestamp
- DELETE → 204 No Content (no body)

----------------------------------------
TASK 2: UI TESTING (Pytest + Playwright)
----------------------------------------

Description:
------------
Automates a simple login scenario using Playwright synchronous API.

Test Website:
-------------
https://the-internet.herokuapp.com/login

Test Scenarios:
---------------
1. test_login_success.py → Verifies successful login with valid credentials.
2. test_login_failure.py → Verifies error message for invalid login.

Steps:
------
1. Open login page
2. Fill in username and password
3. Click "Login" button
4. Validate message visibility and content

Valid Credentials:
------------------
Username: tomsmith  
Password: SuperSecretPassword!

Invalid Credentials:
--------------------
Any other username or password.

Project Layout (UI):
--------------------
<pre>
tests/
│
└── ui/
    ├── conftest.py
    ├── test_login_success.py
    └── test_login_failure.py
</pre>

Installation for UI Tests:
--------------------------
1. Install Playwright and pytest plugin:

   pip install pytest-playwright

2. Install browsers:

   playwright install

Run UI Tests:
-------------
Headless (default):

   pytest tests/ui -v

Headed (with visible browser):

   pytest tests/ui -v --headed --browser=chromium

Assertions:
-----------
- test_login_success.py → checks for "You logged into a secure area!"
- test_login_failure.py → checks for "Your username is invalid!"

----------------------------------------
REQUIREMENTS AND SETUP
----------------------------------------

1. Create a virtual environment:

   python -m venv venv

2. Activate environment:
   macOS/Linux: source venv/bin/activate  
   Windows PowerShell: venv\Scripts\Activate.ps1

3. Install dependencies:

   pip install -r requirements.txt

Example requirements.txt:
-------------------------
pytest  
requests  
pytest-playwright

4. Install browsers (for Playwright):

   playwright install

----------------------------------------
PYTEST CONFIGURATION (pytest.ini)
----------------------------------------

pytest.ini content:
-------------------
[pytest]  
testpaths = tests  
addopts = -v  

markers =  
    api: marks API-related tests  
    ui: marks UI-related tests  

You can run filtered tests:

   pytest -m api  
   pytest -m ui

----------------------------------------
FULL PROJECT STRUCTURE
----------------------------------------

<pre>
python_practice/
├── tests/
│   ├── api/
│   │   ├── conftest.py
│   │   ├── test_get_user.py
│   │   ├── test_post_user.py
│   │   ├── test_put_user.py
│   │   └── test_delete_user.py
│   │
│   └── ui/
│       ├── conftest.py
│       ├── test_login_success.py
│       └── test_login_failure.py
│
├── venv/
├── pytest.ini
├── requirements.txt
└── README.md
</pre>


----------------------------------------
NOTES
----------------------------------------
- API tests use https://reqres.in — a free, public mock API.  
- UI tests use https://the-internet.herokuapp.com/login for demonstration.  
- The Playwright fixture opens a Chromium browser context for each test.  
- Virtual environment (venv/) must be excluded from Git.  

.gitignore example:
-------------------
venv/
__pycache__/
*.pyc
.pytest_cache/
playwright-report/
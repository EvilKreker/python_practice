from playwright.sync_api import Page

def test_login_success(page: Page):
    """
    Test: Successful login on https://the-internet.herokuapp.com/login
    Steps:
      1. Open the login page
      2. Fill in username and password
      3. Click the Login button
      4. Assert that the success message is visible
    """
    # Open login page
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill credentials
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")

    # Click Login
    page.click("button[type='submit']")

    # Assert: success message appears
    success_message = page.locator("#flash")
    assert success_message.is_visible()
    assert "You logged into a secure area!" in success_message.text_content()
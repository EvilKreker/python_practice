from playwright.sync_api import Page

def test_login_failure(page: Page):
    """
    Test: Invalid login attempt
    """
    page.goto("https://the-internet.herokuapp.com/login")

    # Wrong credentials
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpassword")
    page.click("button[type='submit']")

    # Assert: failure message visible
    error_message = page.locator("#flash")
    assert error_message.is_visible()
    assert "Your username is invalid!" in error_message.text_content()
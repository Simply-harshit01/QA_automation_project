# tests/test_login.py
# ─────────────────────────────────────────────────
# Test Suite: Login Functionality
# Site: https://the-internet.herokuapp.com/login
# ─────────────────────────────────────────────────

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config
from utils.logger import get_logger

log = get_logger("test_login")


class TestLogin:
    """
    Test cases for the Login module.

    Test IDs:
        TC_001 — Valid login
        TC_002 — Invalid password
        TC_003 — Invalid username
        TC_004 — Empty username
        TC_005 — Empty password
        TC_006 — Logout after login
    """

    # ── TC_001 ────────────────────────────────────

    def test_valid_login(self, driver):
        """
        TC_001: Verify that a user can log in with valid credentials.

        Steps:
            1. Open login page
            2. Enter valid username and password
            3. Click login button

        Expected: User is redirected to /secure page
        """
        log.info("TC_001: Valid Login")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        assert login_page.is_login_successful(), \
            "Login should succeed with valid credentials"

        dashboard = DashboardPage(driver)
        assert "Secure Area" in dashboard.get_heading_text(), \
            "Dashboard heading should say 'Secure Area'"

    # ── TC_002 ────────────────────────────────────

    def test_login_with_invalid_password(self, driver):
        """
        TC_002: Verify that login fails with wrong password.

        Steps:
            1. Open login page
            2. Enter valid username + invalid password
            3. Click login

        Expected: Error message is displayed; user stays on login page
        """
        log.info("TC_002: Invalid Password")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login(Config.VALID_USERNAME, Config.INVALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "Error message should appear for invalid password"
        assert "/secure" not in driver.current_url, \
            "User should NOT be redirected to secure page"

    # ── TC_003 ────────────────────────────────────

    def test_login_with_invalid_username(self, driver):
        """
        TC_003: Verify login fails with invalid username.
        """
        log.info("TC_003: Invalid Username")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login("invaliduser123", Config.VALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "Error should appear for invalid username"

    # ── TC_004 ────────────────────────────────────

    def test_login_with_empty_username(self, driver):
        """
        TC_004: Verify login fails when username is blank.
        """
        log.info("TC_004: Empty Username")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login("", Config.VALID_PASSWORD)

        assert not login_page.is_login_successful(), \
            "Login should fail with empty username"

    # ── TC_005 ────────────────────────────────────

    def test_login_with_empty_password(self, driver):
        """
        TC_005: Verify login fails when password is blank.
        """
        log.info("TC_005: Empty Password")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login(Config.VALID_USERNAME, "")

        assert not login_page.is_login_successful(), \
            "Login should fail with empty password"

    # ── TC_006 ────────────────────────────────────

    def test_logout_after_valid_login(self, driver):
        """
        TC_006: Verify a logged-in user can successfully log out.

        Steps:
            1. Login with valid credentials
            2. Click Logout
            3. Verify redirected back to /login

        Expected: User is on the login page; logout message shown
        """
        log.info("TC_006: Logout Functionality")

        # Login first
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        assert login_page.is_login_successful()

        # Now logout
        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        # Verify back on login page
        assert "/login" in driver.current_url, \
            "After logout, user should be on the login page"

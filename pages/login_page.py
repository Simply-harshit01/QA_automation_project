# pages/login_page.py
# ─────────────────────────────────────────────────
# Page Object for the Login Page
# URL: https://the-internet.herokuapp.com/login
# ─────────────────────────────────────────────────

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config
from utils.logger import get_logger

log = get_logger("LoginPage")


class LoginPage(BasePage):
    """
    Encapsulates all interactions on the Login page.
    Follows Page Object Model (POM) pattern.
    """

    # ── Locators (what elements to find) ──────────
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE  = (By.ID, "flash")
    SUCCESS_MSG    = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)

    # ── Actions ───────────────────────────────────

    def navigate_to_login(self):
        """Open the login page."""
        self.open(Config.LOGIN_URL)
        log.info("Login page opened")

    def enter_username(self, username: str):
        """Type into the username field."""
        self.type_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password: str):
        """Type into the password field."""
        self.type_text(*self.PASSWORD_FIELD, password)

    def click_login(self):
        """Click the Login button."""
        self.click(*self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """
        High-level action: complete the login flow.
        Usage:
            login_page.login("tomsmith", "SuperSecretPassword!")
        """
        log.info(f"Attempting login with username: '{username}'")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Assertions / Getters ──────────────────────

    def get_flash_message(self) -> str:
        """Return the flash notification message text."""
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """Return True if an error message is visible."""
        msg = self.get_flash_message()
        return "Your username is invalid" in msg or "Your password is invalid" in msg

    def is_login_successful(self) -> bool:
        """Return True if login succeeded (URL changed to /secure)."""
        try:
            self.wait_for_url_contains("/secure")
            return True
        except Exception:
            return False

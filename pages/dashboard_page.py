# pages/dashboard_page.py
# ─────────────────────────────────────────────────
# Page Object for the Secure (Dashboard) Page
# URL: https://the-internet.herokuapp.com/secure
# ─────────────────────────────────────────────────

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

log = get_logger("DashboardPage")


class DashboardPage(BasePage):
    """
    Encapsulates all interactions on the secure dashboard page.
    Accessed after successful login.
    """

    # ── Locators ──────────────────────────────────
    LOGOUT_BUTTON    = (By.CSS_SELECTOR, "a.button.secondary")
    PAGE_HEADING     = (By.TAG_NAME, "h2")
    FLASH_MESSAGE    = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)

    # ── Actions ───────────────────────────────────

    def click_logout(self):
        """Click the Logout button."""
        log.info("Clicking Logout button")
        self.click(*self.LOGOUT_BUTTON)

    # ── Assertions / Getters ──────────────────────

    def get_heading_text(self) -> str:
        """Return the main heading text of the page."""
        return self.get_text(*self.PAGE_HEADING)

    def is_on_secure_page(self) -> bool:
        """Return True if currently on the secure page."""
        try:
            self.wait_for_url_contains("/secure")
            return True
        except Exception:
            return False

    def get_flash_message(self) -> str:
        """Return flash message text (e.g., 'You logged out of...')"""
        return self.get_text(*self.FLASH_MESSAGE)

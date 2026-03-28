# pages/base_page.py
# ─────────────────────────────────────────────────
# Base class for all Page Objects
# Contains reusable Selenium helper methods
# ─────────────────────────────────────────────────

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
from utils.logger import get_logger

log = get_logger("BasePage")


class BasePage:
    """
    Base Page Object — all page classes inherit from this.
    Provides common browser interaction methods.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    # ── Navigation ────────────────────────────────

    def open(self, url: str):
        """Navigate to a URL."""
        log.info(f"Navigating to: {url}")
        self.driver.get(url)

    def get_title(self) -> str:
        """Return current page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Return current page URL."""
        return self.driver.current_url

    # ── Element Interactions ──────────────────────

    def find_element(self, by: By, locator: str):
        """Wait for element and return it."""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except TimeoutException:
            log.error(f"Element not found: ({by}, {locator})")
            raise

    def click(self, by: By, locator: str):
        """Wait for element to be clickable and click it."""
        log.info(f"Clicking element: ({by}, {locator})")
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def type_text(self, by: By, locator: str, text: str):
        """Clear field and type text."""
        log.info(f"Typing '{text}' into element: ({by}, {locator})")
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: By, locator: str) -> str:
        """Get text content of an element."""
        return self.find_element(by, locator).text

    def is_displayed(self, by: By, locator: str) -> bool:
        """Check if element is visible on the page."""
        try:
            return self.find_element(by, locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_url_contains(self, partial_url: str):
        """Wait until the URL contains a specific string."""
        self.wait.until(EC.url_contains(partial_url))

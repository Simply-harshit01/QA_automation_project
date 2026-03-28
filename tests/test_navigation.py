# tests/test_navigation.py
# ─────────────────────────────────────────────────
# Test Suite: Page Navigation & UI Elements
# Site: https://the-internet.herokuapp.com
# ─────────────────────────────────────────────────

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from config.config import Config
from utils.logger import get_logger

log = get_logger("test_navigation")


class TestNavigation:
    """
    Test cases for page navigation and UI element validation.

    Test IDs:
        TC_007 — Home page title
        TC_008 — Login page loads correctly
        TC_009 — Checkboxes page interaction
        TC_010 — Dropdown selection
        TC_011 — JavaScript alert — click OK
        TC_012 — JavaScript alert — click Cancel
    """

    # ── TC_007 ────────────────────────────────────

    def test_home_page_title(self, driver):
        """
        TC_007: Verify the home page loads with the correct title.
        """
        log.info("TC_007: Home page title")

        page = BasePage(driver)
        page.open(Config.BASE_URL)

        assert "The Internet" in driver.title, \
            f"Expected 'The Internet' in title, got: '{driver.title}'"

    # ── TC_008 ────────────────────────────────────

    def test_login_page_elements_present(self, driver):
        """
        TC_008: Verify login page renders all required elements.
        """
        log.info("TC_008: Login page elements")

        login_page = LoginPage(driver)
        login_page.navigate_to_login()

        assert login_page.is_displayed(*LoginPage.USERNAME_FIELD), \
            "Username field should be visible"
        assert login_page.is_displayed(*LoginPage.PASSWORD_FIELD), \
            "Password field should be visible"
        assert login_page.is_displayed(*LoginPage.LOGIN_BUTTON), \
            "Login button should be visible"

    # ── TC_009 ────────────────────────────────────

    def test_checkboxes_interaction(self, driver):
        """
        TC_009: Verify checkboxes can be toggled on the checkboxes page.
        """
        log.info("TC_009: Checkbox interaction")

        page = BasePage(driver)
        page.open(Config.CHECKBOXES_URL)

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        assert len(checkboxes) == 2, "There should be 2 checkboxes on the page"

        # Toggle first checkbox
        initial_state = checkboxes[0].is_selected()
        checkboxes[0].click()
        assert checkboxes[0].is_selected() != initial_state, \
            "First checkbox state should change after click"

    # ── TC_010 ────────────────────────────────────

    def test_dropdown_selection(self, driver):
        """
        TC_010: Verify the dropdown allows selecting an option.
        """
        log.info("TC_010: Dropdown selection")

        from selenium.webdriver.support.ui import Select

        page = BasePage(driver)
        page.open(Config.DROPDOWN_URL)

        dropdown_element = driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)

        dropdown.select_by_visible_text("Option 1")
        assert dropdown.first_selected_option.text == "Option 1", \
            "Option 1 should be selected"

        dropdown.select_by_visible_text("Option 2")
        assert dropdown.first_selected_option.text == "Option 2", \
            "Option 2 should be selected"

    # ── TC_011 ────────────────────────────────────

    def test_javascript_alert_ok(self, driver):
        """
        TC_011: Verify JS alert can be accepted (OK clicked).
        """
        log.info("TC_011: JS Alert - Accept")

        page = BasePage(driver)
        page.open(Config.ALERTS_URL)

        # Click "Click for JS Alert"
        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()

        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Alert", \
            f"Unexpected alert text: {alert.text}"
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        assert "You successfully clicked an alert" in result

    # ── TC_012 ────────────────────────────────────

    def test_javascript_confirm_cancel(self, driver):
        """
        TC_012: Verify JS confirm dialog can be dismissed (Cancel clicked).
        """
        log.info("TC_012: JS Confirm - Dismiss")

        page = BasePage(driver)
        page.open(Config.ALERTS_URL)

        driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()

        alert = driver.switch_to.alert
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        assert "You clicked: Cancel" in result

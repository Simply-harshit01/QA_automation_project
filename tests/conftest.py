# tests/conftest.py
# ─────────────────────────────────────────────────
# Pytest fixtures — shared setup and teardown
# Runs automatically before and after each test
# ─────────────────────────────────────────────────

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from config.config import Config
from utils.logger import get_logger
from utils.screenshot import take_screenshot

log = get_logger("conftest")


@pytest.fixture(scope="function")
def driver(request):
    """
    Sets up the WebDriver before each test and tears it down after.

    - scope="function" means a fresh browser opens for EVERY test
    - Change to scope="class" to share a browser across a test class
    """
    log.info("=" * 60)
    log.info(f"Setting up browser for: {request.node.name}")
    log.info("=" * 60)

    os.makedirs("reports/screenshots", exist_ok=True)

    # ── Initialize Browser ────────────────────────
    # Selenium 4.6+ includes Selenium Manager which auto-downloads
    # the correct ChromeDriver for your OS — no webdriver-manager needed.
    browser = Config.BROWSER.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        # No service needed — Selenium Manager handles the driver automatically
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # ── Browser Settings ──────────────────────────
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    yield driver  # ← Test runs here

    # ── Teardown: Screenshot on Failure ───────────
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        take_screenshot(driver, request.node.name)

    log.info(f"Tearing down browser for: {request.node.name}")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test result (pass/fail) so we can
    take a screenshot on failure in the fixture above.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

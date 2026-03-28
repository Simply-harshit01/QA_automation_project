# config/config.py
# ─────────────────────────────────────────────────
# Central configuration for the QA Automation Framework
# ─────────────────────────────────────────────────

class Config:
    # ── Base URL ──────────────────────────────────
    BASE_URL = "https://the-internet.herokuapp.com"

    # ── Browser Settings ─────────────────────────
    BROWSER = "chrome"          # Options: "chrome", "firefox", "edge"
    HEADLESS = False            # Set True for CI/CD pipelines
    IMPLICIT_WAIT = 10          # seconds
    EXPLICIT_WAIT = 15          # seconds
    PAGE_LOAD_TIMEOUT = 30      # seconds

    # ── Test Credentials ─────────────────────────
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_PASSWORD = "wrongpassword"

    # ── URLs ──────────────────────────────────────
    LOGIN_URL = f"{BASE_URL}/login"
    SECURE_URL = f"{BASE_URL}/secure"
    CHECKBOXES_URL = f"{BASE_URL}/checkboxes"
    DROPDOWN_URL = f"{BASE_URL}/dropdown"
    ALERTS_URL = f"{BASE_URL}/javascript_alerts"

    # ── Report Settings ───────────────────────────
    SCREENSHOT_DIR = "reports/screenshots"
    REPORT_TITLE = "QA Automation Test Report"

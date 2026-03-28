# utils/screenshot.py
# ─────────────────────────────────────────────────
# Captures screenshots on test failure
# ─────────────────────────────────────────────────

import os
from datetime import datetime
from utils.logger import get_logger

log = get_logger("Screenshot")


def take_screenshot(driver, test_name: str) -> str:
    """
    Captures a screenshot and saves it to reports/screenshots/.

    Args:
        driver: Selenium WebDriver instance
        test_name: Name of the test (used in filename)

    Returns:
        Path to the saved screenshot
    """
    screenshot_dir = "reports/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)

    try:
        driver.save_screenshot(filepath)
        log.info(f"Screenshot saved: {filepath}")
    except Exception as e:
        log.error(f"Failed to take screenshot: {e}")

    return filepath

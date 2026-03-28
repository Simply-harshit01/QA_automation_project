# utils/logger.py
# ─────────────────────────────────────────────────
# Custom logger used across all test files
# ─────────────────────────────────────────────────

import logging
import os
from datetime import datetime


def get_logger(name: str = "QAFramework") -> logging.Logger:
    """
    Returns a configured logger instance.
    Usage:
        from utils.logger import get_logger
        log = get_logger(__name__)
        log.info("Test started")
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File Handler
        os.makedirs("reports/logs", exist_ok=True)
        log_file = f"reports/logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        fmt = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(fmt)
        file_handler.setFormatter(fmt)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

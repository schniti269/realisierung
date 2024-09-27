# core/util/logging.py
import logging


def setup_logging():
    """
    Configures logging for the application.
    """
    logging.basicConfig(level=logging.INFO)
    # Additional configuration for Prometheus or other logging handlers can be added here.


def get_logger(name: str):
    """
    Returns a logger instance.
    """
    return logging.getLogger(name)

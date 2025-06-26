import logging
import os
import sys
import traceback

def get_logger(name="ECOM_Logger", log_level=logging.INFO, log_file=None):
    """
    Returns a logger.

    Args:
        name (str): Logger name.
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        log_file (str or None): If provided, logs will also be written to this file.

    Returns:
        logging.Logger: Configured logger instance.
    """
    try:
        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        if not logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

            if log_file:
                try:
                    os.makedirs(os.path.dirname(log_file), exist_ok=True)
                    file_handler = logging.FileHandler(log_file)
                    file_formatter = logging.Formatter(
                        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
                    file_handler.setFormatter(file_formatter)
                    logger.addHandler(file_handler)
                except PermissionError:
                    logger.warning(f"Permission denied: Cannot write to log file '{log_file}'")
                except FileNotFoundError:
                    logger.warning(f"Invalid path: Cannot create or find '{log_file}'")
                except Exception as file_log_err:
                    logger.warning(f"Error setting up file handler: {file_log_err}")

    except Exception as e:
        fallback_logger = logging.getLogger("FallbackLogger")
        if not fallback_logger.handlers:
            fallback_logger.setLevel(logging.ERROR)
            fallback_handler = logging.StreamHandler(sys.stderr)
            fallback_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            fallback_logger.addHandler(fallback_handler)
        fallback_logger.error("Failed to configure logger. Falling back to stderr.", exc_info=True)
        return fallback_logger

    return logger

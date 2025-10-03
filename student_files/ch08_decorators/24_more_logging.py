"""
    24_more_logging.py
    Using a config file with a logger
"""
import logging
import logging.config


logging.config.fileConfig('./logging.ini', disable_existing_loggers=True)

logging.info('Loaded from ini.')
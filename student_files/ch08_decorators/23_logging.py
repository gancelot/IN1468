"""
    23_logging.py
    Using the logging module.
"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='/temp/logfile.log')
logging.debug('Logging started.')


my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)
handler1 = logging.FileHandler('./lab05_logfile.log')
formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M:%S')
handler1.setFormatter(formatter)
my_logger.addHandler(handler1)

# handler 2 is used to log to the console if desired
handler2 = logging.StreamHandler()
handler2.setFormatter(formatter)
my_logger.addHandler(handler2)

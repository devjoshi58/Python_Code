#Using the logging.conf

import logging
import logging.config
"""
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
"""

logging.config.fileConfig('/Users/varunjoshi/Documents/GitHub/Python_Code/Logging/logging.conf')
logger = logging.getLogger('sampleLogger')
logger.debug("message for debug")



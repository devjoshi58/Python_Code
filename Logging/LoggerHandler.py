#Creating handlers for logger

import logging

logger = logging.getLogger(__name__)

#create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#Set level for each handler

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#format the logs

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('warning message')
logger.error('error message')

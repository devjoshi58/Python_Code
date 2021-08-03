import logging

#We use basicconfig to print the logs in particular format
#Here it is using the root logger


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is a info messagr')
#By default only log with warning or above gets printed
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('Thus is a critical message')

 
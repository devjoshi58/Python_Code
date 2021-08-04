import logging

try:
    a= [1,2,34]
    print(a[4])
except Exception as e:
    logging.error(e,exc_info=True) #USE exc_info as True to print stack trace

#Using the traceback method

import traceback

try:
    a= [1,2,34]
    print(a[4])
except:
    logging.error("this error is %s",traceback.format_exc())


import os
import logging

def prepare_logger():
    print 'prepare logger'
    logger = logging.getLogger('root')
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    logger.setLevel(logging.DEBUG)

    return logger

class config:
    configrations = {}
    logger = prepare_logger()

    def __init__(self):
        prepare_logger()

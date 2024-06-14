# Common libraries
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))) 

from logyca import Logger

logger=Logger()

def main_run():
    msg="ms1"
    logger.critical(msg)
    logger.debug(msg)
    logger.error(msg)
    logger.info(msg)
    logger.warning(msg)

import logging
from satcog.config import Config

def load_logger():

logging.config.fileConfig(Config, disable_existing_loggers=True)

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')
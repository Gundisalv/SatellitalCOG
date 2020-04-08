import logging
import logging.config

from satcog.config import Config


def load_logger():
    logging.config.fileConfig(Config, disable_existing_loggers=True)

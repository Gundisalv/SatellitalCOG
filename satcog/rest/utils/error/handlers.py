from flask import current_app

from satcog.rest import api


@api.errorhandler
def handle_default(e: Exception) -> (dict, int):
    current_app.logger.exception(e)

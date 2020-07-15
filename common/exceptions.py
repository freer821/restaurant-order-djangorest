from rest_framework.views import exception_handler

from config.middleware import getStandardResponse

import logging
logger = logging.getLogger(__name__)

def whs_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        logger.error(response.data)
        response.data = getStandardResponse(500, '', response.data)

    return response

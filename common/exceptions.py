from rest_framework.response import Response

from config.middleware import getStandardResponse
from .utils import logger

def whs_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    logger.error(exc)
    return Response(getStandardResponse(500, '系统出错，请联系客服！'))
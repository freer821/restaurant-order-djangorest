from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import exceptions

from config.middleware import getStandardResponse
from .utils import logger
import sys

def whs_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    elif not isinstance(exc, WHSException):
        exc = Exception('系统出错，请联系客服')

    logger.error(str(exc))
    return Response(getStandardResponse(500, str(exc)))


class WHSException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
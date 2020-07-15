import socket

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from common.utils import logger

def getStandardResponse(status, msg='', data=''):
    return {
        'status': status,
        'msg': msg,
        'data': data
    }

class WHSRequestResponseMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(WHSRequestResponseMiddleware, self).__init__(*args, **kwargs)

    def process_template_response(self, request, response):
        try:
            log_data = {
                'user': request.user,

                'remote_address': request.META['REMOTE_ADDR'],
                'server_hostname': socket.gethostname(),

                'request_method': request.method,
                'request_path': request.get_full_path(),
                'request_body': request.body,

                'response_status': response.status_code,
            }
            logger.info(log_data)
        except Exception as e:
            logger.error(e)

        if not response.is_rendered and isinstance(response, Response):
            if isinstance(response.data, dict):

                keys = response.data.keys()
                if "swagger" in keys:
                    return response

                if "status" in keys and "msg" in keys:
                    return response
                else:
                    if response.status_code < 300:
                        response.data = getStandardResponse(200, '', response.data)
                    else:
                        response.data = getStandardResponse(response.status_code, response.data)

                    response.status_code = 200
            elif response.status_code < 300:
                response.status_code = 200
                response.data = getStandardResponse(200)
            else:
                response.status_code = 200
                response.data = getStandardResponse(500)

        return response


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
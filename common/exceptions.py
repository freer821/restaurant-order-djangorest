from rest_framework.views import exception_handler

from config.middleware import getStandardResponse


def whs_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        print(response.data)
        response.data = getStandardResponse(500, '', response.data)

    return response

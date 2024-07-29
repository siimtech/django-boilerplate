import threading
from django.http import HttpResponse

_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, 'request', None)

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        response = self.get_response(request)
        # print("is_superuser", request.user.is_superuser)
        # if request.user.is_superuser is False:
        #     response = HttpResponse('Service Unavailable', status=503)
        return response
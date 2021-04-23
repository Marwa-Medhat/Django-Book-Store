from django.http import HttpResponseForbidden


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # request.user.is_authenticated
        # request.user.username
        if request.user.username:
            if request.user.is_staff:
                return self.get_response(request)
            else:
                return HttpResponseForbidden("you are not an active user,please contact the adminstration")
        else:
            return self.get_response(request)

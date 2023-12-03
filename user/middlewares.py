def my_middleware(get_response):
    # One time initialization
    def middleware_fun(request):
        # Code that runs before each request to modify the incoming request
        response = get_response(request)
        # Code that runs after each request, regardless of whether an exception was raised or not.
        return response
    return middleware_fun


class ClassBased():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

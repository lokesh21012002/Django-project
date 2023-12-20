from rest_framework.exceptions import APIException


class CustomeException(APIException):
    status_code = 200
    default_detail = "Custom Error"

    def __init__(self, detail=None, status_code=None, **kwargs):
        self.detail = detail or self.default_detail
        self.status_code = status_code or self.status_code
        super().__init__(**kwargs)

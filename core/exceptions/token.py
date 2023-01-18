from core.exceptions import CustomException


class UserCheckException(CustomException):
    code = 400
    error_code = "credential error"
    message = "username or password not correct"


class DecodeTokenException(CustomException):
    code = 400
    error_code = "TOKEN__DECODE_ERROR"
    message = "token decode error"


class ExpiredTokenException(CustomException):
    code = 400
    error_code = "TOKEN__EXPIRE_TOKEN"
    message = "expired token"

class CustomExpiredTokenException(CustomException):
    code = 400

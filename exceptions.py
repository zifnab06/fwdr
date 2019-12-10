from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated", 401,
            {"WWW-Authenticate": "Basic realm=\"Login Required\""}
            ))

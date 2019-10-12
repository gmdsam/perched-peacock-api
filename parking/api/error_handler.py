from functools import wraps
import traceback
import sys
from flask import jsonify
from flask_restplus import abort


def error_handler(f):
    """
    Custom error handler used for outputting formatted errors in API.
    In case of ValueError / TypeError, it raises a 400 error code with a JSON containing the error message / stack.
    """
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            resp = f(*args, **kwds)
            return resp
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            exc_info = {
                'stackTrace': traceback.format_exception(exc_type, exc_value, exc_traceback)
            }
            abort(code=400, message=str(e), **exc_info)

    return wrapper


def handle_value_error(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    response = jsonify({
        'message': error.message,
        'stackTrace': traceback.format_exception(exc_type, exc_value, exc_traceback)
    })
    response.status_code = 400
    return response

import flask
from flask import jsonify
blueprint = flask.Blueprint('errors', __name__)


# --- Parent Error Class ---    

class BaseError(Exception):

    def __init__(self, status=400, detail='', title='', field=None):
        Exception.__init__(self)
        self.status = status
        self.detail = detail
        self.title = title
        self.field = field

    def to_dict(self):
        return {'title': self.title,
                'status': self.status,
                'detail': self.detail,}


  
# --- Child Error Classes ---    

# This Error is for unauthorized access (wrong password or token etc...). Not implemented in current code
class NotAuthorizedError(BaseError):
    def __init__(self, detail='Unauthorized'):
        BaseError.__init__(self)
        self.status = 401
        self.detail = detail
        self.title = 'Access Unauthorized'

# This Error is for invalid input data
class ValidationError(BaseError):
    def __init__(self, detail='Input is not Valid'):
        BaseError.__init__(self)
        self.status = 400
        self.detail = detail
        self.title = 'Invalid Input'
      


# --- Defining Error Handlers for custom errors---    

@blueprint.app_errorhandler(NotAuthorizedError)
@blueprint.app_errorhandler(ValidationError)
def handle_error(error):
    return jsonify(error.to_dict()), getattr(error, 'status')



# --- Error handling for default http error(s) ---

@blueprint.app_errorhandler(404)
def handle_unexpected_error(error):
    response =  {'title': 'Wrong endpoint',
                'status': '404',
                'detail': 'Wrong endpoint being used. Please use /detect_glare endpoint for posting metadata',}
    return jsonify(response), 404

@blueprint.app_errorhandler(405)
def handle_unexpected_error(error):
    response =  {'title': 'Method Not Allowed',
                'status': '405',
                'detail': 'This method is not allowed. Only supported methods are currently: POST',}
    return jsonify(response), 405



# --- Error handling for unexpected errors ---

@blueprint.app_errorhandler(Exception)
def handle_unexpected_error(error):
    response =  {'title': 'Unexpected Error',
                'status': '500',
                'detail': 'An unexpected error has occured. Please try again later and report this error to osman@alumni.ubc.ca',}
    return jsonify(response), 500







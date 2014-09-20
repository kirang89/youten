from functools import wraps

from flask import request, Blueprint, jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from api.errors import *


api_v1 = Blueprint('v1', __name__)


######################## Authentication ################################

def requires_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
	pass
    return wrapper

############################# Views ####################################


@api_v1.route('/meta', methods=['GET'])
def index():
    data = {
        "name": "My API",
        "version": "1.0",
        "organisation": "Me only",
        "description": "this is version 1.0 of my api!"
    }
    return jsonify(data)

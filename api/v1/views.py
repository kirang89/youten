from functools import wraps

from flask import request, Blueprint, jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from api.errors import *
from api.models import Snippet


api_v1 = Blueprint('v1', __name__)


######################## Authentication ################################

def requires_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper

############################# Views ####################################


@api_v1.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@api_v1.route('/meta', methods=['GET'])
@requires_authentication
def index():
    data = {
        "name": "My API",
        "version": "1.0",
        "organisation": "Me only",
        "description": "this is version 1.0 of my api!"
    }
    return jsonify(data)


@api_v1.route('/snippets', methods=['POST'])
@requires_authentication
def save_snippet():
    if request.json:
        snippet = Snippet(title=request.json['title'],
                          language=request.json['language'],
                          code=request.json['snippet'])
        db.session.add(snippet)
        db.session.commit()
    else:
        return not_acceptable('Please ensure that your request contains a valid JSON')


@api_v1.route('/snippets', methods=['GET'])
@requires_authentication
def get_all_snippets():
    snippets = Snippets.query.all()
    data['snippets'] = []
    for snippet in snippets:
        data[snippets].append(snippet.get_public())
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')


@api_v1.route('/snippets/language/<language>', methods=['GET'])
@requires_authentication
def get_all_snippets_for_language(language):
    snippets = Snippets.query.filter_by(language=language).all()
    data['snippets'] = []
    for snippet in snippets:
        data[snippets].append(snippet.get_public())
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')


@api_v1.route('/snippets/<snippet_id>', methods=['DELETE'])
@requires_authentication
def delete_snippet(snippet_id):
    snippet = Session.query.get(snippet_id)
    if snippet:
        db.session.delete(snippet)
        db.session.commit()

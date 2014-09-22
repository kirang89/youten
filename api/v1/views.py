from functools import wraps
from flask import request, Blueprint, jsonify
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
def index():
    data = {
        "name": "My API",
        "version": "1.0",
        "organisation": "Me only",
        "description": "this is version 1.0 of my api!"
    }
    return jsonify(data)


@api_v1.route('/snippets', methods=['POST'])
def save_snippet():
    if request.json:
        snippet = Snippet(title=request.json['title'],
                          language=request.json['language'],
                          code=request.json['snippet'])
        db.session.add(snippet)
        db.session.commit()
        return Response(json.dumps({"id": snippet.id}),
                        201,
                        mimetype='application/json')
    else:
        return not_acceptable('Please ensure that your request contains a valid JSON')


@api_v1.route('/snippets', methods=['GET'])
def get_all_snippets():
    data = {}
    data['snippets'] = []
    snippets = Snippet.query.all()
    for snippet in snippets:
        data['snippets'].append(snippet.get_dict())
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')


@api_v1.route('/snippets/language/<language>', methods=['GET'])
def get_all_snippets_for_language(language):
    data = {}
    data['snippets'] = []
    snippets = Snippet.query.filter_by(language=language).all()
    for snippet in snippets:
        data[snippets].append(snippet.get_public())
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')


@api_v1.route('/snippets/<snippet_id>', methods=['DELETE'])
def delete_snippet(snippet_id):
    snippet = Session.query.get(snippet_id)
    if snippet:
        db.session.delete(snippet)
        db.session.commit()

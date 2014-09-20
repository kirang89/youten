import json
from flask import Response
from v1.views import api_v1
from api import app, db
from api.errors import *


app.register_blueprint(api_v1, url_prefix='/v1')


@app.route('/', methods=['GET'])
def index():
    data = {
        "message": "Youten!"
    }
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')

from api import db
from api.helpers import Serializer
import uuid
from datetime import datetime


class Snippet(db.Model, Serializer):
    """A code snippet"""
    __tablename__ = 'snippets'
    __public__ = ('id', 'code', 'title',
                  'language', 'created_at', 'updated_at')
    id = db.Column(db.String, primary_key=True, unique=True)
    code = db.Column(db.Text)
    title = db.Column(db.Text)
    language = db.Column(db.Text)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __init__(self, title, language, code):
        self.id = uuid.uuid4().hex
        self.title = title
        self.language = language
        self.code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_code(self, code):
        self.code = code
        self.updated_at = datetime.now()

    def __repr__(self):
        return '<Snippet [{}]: {}>'.format(self.id, self.title)

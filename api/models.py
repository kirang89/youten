from api import db
from api.helpers import Serializer
import uuid


class Snippet(db.Model, Serializer):
    """A code snippet"""
    __tablename__ = 'snippets'
    __public__ = ('id', 'code', 'title', 'language')
    id = db.Column(db.String, primary_key=True, unique=True)
    code = db.Column(db.Text)
    title = db.Column(db.Text)
    language = db.Column(db.Text)

    def __init__(self, title, language, code):
        self.id = uuid.uuid4().hex
        self.title = title
        self.language = language
        self.code = code

    def __repr__(self):
        return '<Snippet [{}]: {}>'.format(self.id, self.title)

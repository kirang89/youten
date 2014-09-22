from api import app, db
from api.models import Snippet
import unittest


class APIv1Test(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.load_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def load_data(self):
        snippet = Snippet(title="Uploading a file to S3 using Boto",
                          language="python",
                          code="""
                            import cStringIO
                            from boto.s3.connection import S3Connection
                            from boto.s3.key import Key


                            def s3upload(filename, extension, file):
                                conn = S3Connection('AWS_ACCESS_KEY', 'AWS_SECRET_KEY')
                                k = Key(conn.get_bucket('<bucket name>'))
                                k.key = filename
                                k.set_metadata("Content-Type", file.mimetype)
                                fp = cStringIO.StringIO(file.read())
                                k.set_contents_from_file(fp)
                                k.set_acl("public-read")
                                fp.close()
                                return "https://s3.amazonaws.com/<bucket name>/{}.{}".format(filename, extension)
                          """)
        print snippet.id
        db.session.add(snippet)
        db.session.commit()

    def test_index(self):
        res = self.app.get('/v1/meta')
        self.assertEqual(res.status_code, 200)

